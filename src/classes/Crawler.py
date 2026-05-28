import config
import logging
import requests
import time
import utils
from .Baseliner import Baseliner
from .Dataclasses import Validity
from .Documentor import Documentor
from .Requester import Requester
from .Seeder import Seeder
from classes.models.BaseModel import BaseModel
from typing import Any


logger = logging.getLogger(__name__)


class Crawler:


    def __init__(self, llm: BaseModel, api_config: dict[Any, Any]) -> None:
        """
        Initializes the Crawler class instance.

        Args:
            llm: The LLM class instance to use to send prompts.
            api_config: The configuration parameters for the API.
        """

        self.llm = llm
        self.api_config = api_config
        self.api_name = api_config.get("name", "Unknown API Name")
        self.api_id = self.api_name.lower().replace(" ", "-")
        self.endpoint = self.api_config["base-url"].strip().rstrip("/")
        self.methods_to_check = config.EXECUTION.get("methods-to-check", ["get", "post", "put", "patch", "delete"])
        self.methods_fallback = config.EXECUTION.get("methods-fallback", ["get"])
        self.max_infer_elements = config.EXECUTION.get("max-infer-elements", 20)

        # initialize dictionary which will be used to store execution data
        self.execution = {}

        # class instances
        self.baseliner = Baseliner(self.api_config)
        self.documentor = Documentor(self.llm, self.api_config, self.api_name, self.api_id, self.endpoint)
        self.requester = Requester()
        self.seeder = Seeder(self.api_id)


    def execute(self) -> None:
        """
        Executes the crawler pipeline.

        (1) Starts a timer and generates basic documentation data (metadata and servers).
        (2) Starts the crawling process.
        (3) Ends the timer and saves the execution data.
        """

        logger.info(f"Starting execution for: {self.api_id}")

        start_time = time.time()

        self.documentor.document_metadata()
        self.documentor.document_servers()

        self.crawl()

        end_time = time.time()

        execution_time = end_time - start_time
        
        self.execution = {
            "timestamp": config.TIMESTAMP,
            "execution-time-seconds": execution_time,
            "api": {
                "nb-requests": self.requester.nb_requests,
                "baseline": self.baseliner.baseline
            },
            "llm": {
                "llm-id": self.llm.llm_id,
                "temperature": self.llm.temperature,
                "nb-prompts": self.llm.nb_prompts,
                "tokens": self.llm.tokens
            }
        }

        self.save()

        logger.info(f"Finished execution for: {self.api_id}")


    def save(self) -> None:
        """
        Saves the execution data, seeds, and generated documentation.
        """

        execution_out_path = config.OUT_PATH / self.api_id / "execution.json"
        utils.save_json(execution_out_path, self.execution)
        self.seeder.save()
        self.documentor.save()


    def crawl(self) -> None:
        """
        Crawls the REST API by inferring keywords, common paths, base paths, and mutations.
        """

        # (1) infer URLs with keywords related to the API subject/topic
        self.infer_keywords()

        # (2) infer URLs with common paths
        self.infer_common_paths()

        # (3) infer URLs with paths of the API known by the LLM
        self.infer_base_paths()

        # (4) infer remaining URLs with the seed mutation process
        self.infer_mutations()


    def infer_keywords(self) -> None:
        """
        Infers URLs with paths consisting of keywords related to the API subject/topic.
        The LLM is used to generated the vocabulary of relevant keywords.
        """

        infer_keywords = config.EXECUTION.get("infer-keywords", False)

        if not infer_keywords:
            return

        logger.info("Inferring paths with keywords")

        keywords_prompt = config.PROMPTS["keywords"].format(api_name=self.api_name)
        keywords_str = self.llm.prompt(keywords_prompt)
        keywords_paths = self.sanitize_paths(keywords_str)

        for path in keywords_paths:
            url = f"{self.endpoint}/{path}"
            self.infer_url(url)


    def infer_common_paths(self) -> None:
        """
        Infers URLs with paths that are commonly found in REST APIs.
        The vocabulary for common paths is from a raw .txt file, which can be modified.
        """

        infer_common_paths = config.EXECUTION.get("infer-common-paths", False)

        if not infer_common_paths:
            return

        logger.info("Inferring common paths")

        common_paths = config.COMMON_PATHS

        for path in common_paths:
            url = f"{self.endpoint}/{path}"
            self.infer_url(url)


    def infer_base_paths(self) -> None:
        """
        Infers URLs with paths of the API known by the LLM.
        """

        logger.info("Inferring base paths")

        # start to try and infer the API endpoint
        self.infer_url(self.endpoint)

        # then, infer paths
        base_prompt = config.PROMPTS["paths"].format(api_name=self.api_name)
        base_str = self.llm.prompt(base_prompt)
        base_paths = self.sanitize_paths(base_str)

        for path in base_paths:
            url = f"{self.endpoint}/{path}"
            self.infer_url(url)


    def infer_url(self, url: str) -> None:
        """
        Infers a given URL.

        (1) The OPTIONS method is used to find the HTTP methods that are supported by the URL.
        (2) Requests using the supported methods are sent to the API server.
        (3) The validity of requests is verified, and added to valid/invalid seeds.
        (4) The function attempts to infer query parameters.

        Args:
            url: The URL to be inferred.
        """

        # small preliminary sanitization
        url = url.strip().rstrip("/").replace("/?", "?")

        # if the URL already exists in the seeds, do not infer
        if self.seeder.exists_in_seeds(url, "options", only_path=True):
            return

        supported_methods = self.requester.get_url_methods(url)

        if supported_methods:
            self.seeder.add_seed(url, "options", Validity("valid", "supported methods found"))

        # if there are no supported methods (i.e., the OPTIONS method did not yield any), still attempt to infer URLs with the fallback methods
        else:
            self.seeder.add_seed(url, "options", Validity("invalid", "no supported methods found"))
            supported_methods = self.methods_fallback

        for method in supported_methods:
            # if the method should not be checked (based on the configuration file) or if it already exists in the seeds, skip it
            if method not in self.methods_to_check or self.seeder.exists_in_seeds(url, method):
                continue

            # generate a payload only for POST, PUT, and PATCH methods
            payload = None
            if method in ["post", "put", "patch"]:
                payload = self.generate_payload(url, method)

            response = self.requester.send_request(url, method, payload)

            # if a request error occurred (unrelated to the client-server interaction), skip it
            if response is None:
                continue

            validity = self.requester.check_response(response)
            self.seeder.add_seed(url, method, validity)

            # if the URL is valid, infer it into the documentation
            if validity.category == "valid":
                self.documentor.document_request(url, method, response, payload)
                self.baseliner.check(url, method)

                # try to find query parameters for the request
                self.infer_query_parameters(url, method, response)


    def infer_query_parameters(self, url: str, method: str, response: requests.Response) -> None:
        """
        Infers query parameters for a given URL.
        The process works by taking an URL without any query parameters, storing its current response, and adding query parameters.
        By comparing the response obtained with and without the query parameters, we can have an idea of their validity and infer them.
        This process does not always work and is still experimental.

        Args:
            url: The URL of the request.
            method: The HTTP method of the request.
            response: The response obtained for the request.
        """

        query_parameters_prompt = config.PROMPTS["query-parameters"].format(api_name=self.api_name, http_method=method.upper(), url=url)
        query_parameters_str = self.llm.prompt(query_parameters_prompt)
        query_parameters = self.sanitize_query_parameters(query_parameters_str)

        for query_parameter in query_parameters:
            separator = "&" if "?" in url else "?"
            new_url = f"{url}{separator}{query_parameter}"

            if self.seeder.exists_in_seeds(new_url, method):
                continue

            new_response = self.requester.send_request(new_url, method)

            if new_response is None:
                continue

            validity = self.requester.check_response(new_response, response)
            self.seeder.add_seed(new_url, method, validity)

            if validity.category == "valid":
                self.documentor.document_request(new_url, method, new_response)
                self.baseliner.check(new_url, method)


    def infer_mutations(self) -> None:
        """
        Infers URLs based on a seed mutation process.
        """

        # if there are no valid seeds, there is no point to mutate so stop
        if self.seeder.only_invalid():
            logger.warning("Could not mutate as no valid seed(s) exist")
            return

        seed_index = 0
        mutation_index = 0
        max_mutations = config.EXECUTION.get("max-mutations", 10)

        while mutation_index <= max_mutations:
            seed = self.seeder.seeds[seed_index]
            logger.info(f"Mutation budget {mutation_index}/{max_mutations}, Seed {seed_index}/{len(self.seeder.seeds)}")

            # update the seed index by incrementing its value by 1 ; if at the end of the list, reset to 0
            seed_index = (seed_index + 1) % len(self.seeder.seeds)

            # to avoid mutations of OPTIONS methods or other unwanted methods that may have ended up in the seed list
            if seed.http_method not in self.methods_to_check:
                continue

            # select the first seed variant which is valid
            seed_variant = None
            for variant in seed.variants:
                if variant.validity.category == "valid":
                    seed_variant = variant

            # if no valid seed variant was found, skip the seed
            if not seed_variant:
                continue

            self.infer_add_route_mutation(seed_variant.url, seed.http_method)
            self.infer_modify_route_mutation(seed_variant.url, seed.http_method)

            mutation_index += 1


    def infer_add_route_mutation(self, url: str, method: str) -> None:
        """
        Infers URLs based on the "add route" mutation.

        Args:
            url: The URL of the request.
            method: The HTTP method of the request.
        """

        path_placeholder = "<path>"

        if "?" in url:
            path, query = url.split("?", 1)
            query = f"?{query}"
        else:
            path = url
            query = ""

        masked_url = f"{path}/{path_placeholder}{query}"
        prompt = config.PROMPTS["placeholder-path"].format(api_name=self.api_name, http_method=method.upper(), url=masked_url)
        response = self.llm.prompt(prompt)
        paths = self.sanitize_paths(response)

        for path in paths:
            if path:
                mutated_url = masked_url.replace(path_placeholder, path)
                self.infer_url(mutated_url)


    def infer_modify_route_mutation(self, url: str, method: str) -> None:
        """
        Infers URLs based on the "modify route" mutation.

        Args:
            url: The URL of the request.
            method: The HTTP method of the request.
        """

        path_placeholder = "<path>"

        if "?" in url:
            path, query = url.split("?", 1)
            query = f"?{query}"
        else:
            path = url
            query = ""

        masked_url = url.rsplit("/", 1)[0] + "/" + path_placeholder + query
        prompt = config.PROMPTS["placeholder-path"].format(api_name=self.api_name, http_method=method.upper(), url=masked_url)
        response = self.llm.prompt(prompt)
        paths = self.sanitize_paths(response)
        
        for path in paths:
            if path:
                mutated_url = masked_url.replace(path_placeholder, path)
                self.infer_url(mutated_url)


    def generate_payload(self, url: str, method: str) -> dict[Any, Any]:
        """
        Generates a payload for a given HTTP request.

        Args:
            url: The URL of the request.
            method: The HTTP method of the request.

        Returns:
            The generated payload for the request.
        """

        payload_prompt = config.PROMPTS["payload"].format(api_name=self.api_name, http_method=method.upper(), url=url)
        payload_str = self.llm.prompt(payload_prompt)

        payload = {}

        if payload_str is not None:
            payload = utils.str_to_json(payload_str)

        return payload


    def remove_path_overlap_with_base(self, path: str) -> str:
        """
        Removes any overlap a path might have with the API base URL.
        Example: If the base URL is 'https://api.gbif.org/v1/species' and the path is '/v1/species/match', the latter will be simplified into 'match'.

        Args:
            path: The path from which to remove the overlap.

        Returns:
            The path without any overlap wrt the base URL.
        """

        # in the event that the path is a full URL, remove "www." for compatibility
        path = path.replace("www.", "")
        # replace HTTP by HTTPS
        if "https" not in path:
            path = path.replace("http", "https")

        base = self.endpoint
        base_parts = base.strip("/").split("/")
        path_parts = path.strip("/").split("/")

        for i in range(min(len(base_parts), len(path_parts)), 0, -1):
            if base_parts[-i:] == path_parts[:i]:
                path_parts = path_parts[i:]
                break

        return "/".join(path_parts)


    def sanitize_query_parameters(self, query_parameters_str: str | None) -> list[str]:
        """
        Sanitizes a string of query parameters separated by commas into a list of query parameters.
        For each query parameter, the function:
        (1) Replaces spaces with "+" symbols
        (2) Checks for value presence
        (3) Do not keep query parameter names that were already added
        (4) Limit final list size based on config

        Args:
            query_parameters_str: The string of query parameters.

        Returns:
            The list of query parameters to keep, that were extracted from the string of query parameters.
        """

        if query_parameters_str is None or query_parameters_str == "":
            return []
        
        query_parameters = query_parameters_str.replace("\n", ",").split(",")
        query_parameter_names = []
        query_parameters_keep = []

        for query_parameter in query_parameters:
            # (1) replace spaces with '+' for URL validity
            query_parameter = query_parameter.strip().replace(" ", "+")

            # (2) check if value exists after "=", otherwise remove it
            if "=" not in query_parameter:
                continue
            #if query_parameter[-1] == "=":
                #query_parameter = query_parameter[:-1]

            # (3) prevent duplicate parameter names
            parameter_name = query_parameter.split("=")[0]

            if parameter_name not in query_parameter_names:
                query_parameters_keep.append(query_parameter)
                query_parameter_names.append(parameter_name)

        # (4) limit final list size
        query_parameters_keep = query_parameters_keep[:self.max_infer_elements]

        logger.info(f"Sanitized query parameters: {query_parameters_keep}")

        return query_parameters_keep


    def sanitize_paths(self, paths_str: str | None) -> list[str]:
        """
        Sanitizes a string of paths separated by commas into a list of paths.
        For each path, the function:
        (1) Removes leading/trailing whitespaces and '/'
        (2) Replaces spaces with '+' for URL validity
        (3) Removes any overlap the path may have with the API endpoint base URL
        (4) Limit final list size based on config

        Example: If a path string is '/species?id=2, /lookup/id', it will be sanitized as ['species?id=2', 'lookup/id']

        Args:
            paths_str: The string of paths.

        Returns:
            The list of paths to keep, that were extracted from the string of paths.
        """

        if paths_str is None or paths_str == "":
            return []

        paths = paths_str.replace("\n", ",").split(",")
        paths_keep = []

        for path in paths:
            # (1) remove leading and trailing whitespaces and '/' from paths as they will be added in the URL construction
            path = path.strip(" /")
            # (2) replace spaces with '+' for URL validity
            path = path.replace(" ", "+")
            # (3) remove path overlap with API endpoint base URL
            path = path.replace(self.endpoint, "")
            path = self.remove_path_overlap_with_base(path)

            if path not in paths_keep:
                paths_keep.append(path)

        # (4) limit final list size
        paths_keep = paths_keep[:self.max_infer_elements]

        logger.info(f"Sanitized paths: {paths_keep}")

        return paths_keep