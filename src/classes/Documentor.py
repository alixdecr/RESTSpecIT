import config
import copy
import logging
import requests
import utils
from classes.models.BaseModel import BaseModel
from typing import Any


logger = logging.getLogger(__name__)


class Documentor:


    def __init__(self, llm: BaseModel, api_config: dict[Any, Any], api_name: str, api_id: str, endpoint: str) -> None:
        """
        Initializes the Documentor class instance.

        Args:
            llm: The LLM class instance to use to send prompts.
            api_config: The configuration parameters for the API.
            api_name: The name of the API.
            api_id: The identifier of the API.
            endpoint: The URL for the endpoint of the API.
        """

        self.llm = llm
        self.api_config = api_config
        self.api_name = api_name
        self.api_id = api_id
        self.endpoint = endpoint

        # in case the endpoint has paths, find its base
        protocol, rest = endpoint.split("//", 1)
        domain = rest.split("/", 1)[0]
        self.base = f"{protocol}//{domain}"

        self.oas = copy.deepcopy(config.OAS_TEMPLATE)
        self.generate_descriptions = config.EXECUTION.get("generate-descriptions", True)

        self.method_verbs = {
            "get": "retrieves",
            "post": "creates",
            "put": "replaces or creates",
            "patch": "modifies",
            "delete": "removes"
        }


    def document_metadata(self) -> None:
        """
        Documents the overall metadata of the API.
        """

        # title
        self.oas["info"]["title"] = f"{self.api_name} - OpenAPI Specification"

        # description
        if self.generate_descriptions:
            api_description_prompt = config.PROMPTS["api-description"].format(api_name=self.api_name)
            api_description = self.llm.prompt(api_description_prompt)
            self.oas["info"]["description"] += f"\n{api_description}"


    def document_servers(self) -> None:
        """
        Documents the server metadata fields of the API.
        """

        # try to find if the server URL is online or local
        available = "online" if "localhost" not in self.base else "local"

        self.oas["servers"] = [
            {
                "url": self.base,
                "description": f"{available.capitalize()} server URL of the '{self.api_name}' REST API."
            }
        ]


    def document_request(self, url: str, method: str, response: requests.Response, payload: dict[Any, Any] | None = None) -> None:
        """
        Documents a given HTTP request for the API.

        Args:
            url: The URL of the request.
            method: The HTTP method of the request.
            response: The response obtained when sending the request to the server.
            payload: An optional payload accompanying the request.
        """

        path = utils.get_canonical_url(url, include_query=False).replace(self.base, "")
        
        # if the path does not yet exist, create it
        if path not in self.oas["paths"]:
            self.oas["paths"][path] = {}

        # if the HTTP method associated with the path does not yet exist, create it
        if method not in self.oas["paths"][path]:
            method_verb = self.method_verbs[method]
            summary = f"{method_verb.capitalize()} data at the path {path}."
            description_str = "Description goes here."

            if self.generate_descriptions:
                description_prompt = config.PROMPTS["route-description"].format(api_name=self.api_name, http_method=method.upper(), path=path)
                description_str = self.llm.prompt(description_prompt)

            operation_id = f"{method}{utils.str_to_pascal_case(path)}"
            status_code = str(response.status_code)
            response_body = response.text

            self.oas["paths"][path][method] = {
                "summary": summary,
                "description": description_str,
                "parameters": [],
                "operationId": operation_id,
                "responses": {
                    f"{status_code}": {
                        "description": "Successful operation.",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object"
                                },
                                "example": response_body
                            }
                        }
                    },
                    "default": {
                        "description": "Unexpected error.",
                    }
                }
            }

            # if the path contains a path parameter, document it
            if "{" in path and "}" in path:
                self.document_path_parameters(path, method)

            # if the path requires a payload, document it
            if payload is not None:
                self.document_request_body(path, method, payload)

        # if the request has query parameters, document them
        if "?" in url:
            query_parameters = url.split("?")[1].split("&")

            for query_parameter in query_parameters:
                self.document_query_parameter(query_parameter, path, method)


    def document_request_body(self, path: str, method: str, payload: dict[Any, Any]) -> None:
        """
        Documents a requestBody field for a path and method with the content of the payload.

        Args:
            path: The API path.
            method: The HTTP method used with the path.
            payload: The payload example that was used with the method and path.
        """

        self.oas["paths"][path][method]["requestBody"] = {
            "description": f"Request body or payload.",
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object"
                    },
                    "example": payload
                }
            }
        }


    def document_path_parameters(self, path: str, method: str) -> None:
        """
        Documents path parameters for a path and method.

        Args:
            path: The API path.
            method: The HTTP method used with the path.
        """

        for part in path.split("/"):

            if "{" not in part or "}" not in part:
                continue

            name = "digits"
            schema = {
                "type": "integer",
                "example": 1
            }

            if "{country-code}" in path:
                name = "country-code"
                schema["type"] = "string"
                schema["example"] = "CA"

            elif "{file}" in path:
                name = "file"
                schema["type"] = "string"
                schema["example"] = "my_file.ext"

            elif "{uuid}" in path:
                name = "uuid"
                schema["type"] = "string"
                schema["example"] = "550e8400-e29b-41d4-a716-446655440000"

            elif "{version}" in path:
                name = "version"
                schema["type"] = "string"
                schema["example"] = "v1.2"

            self.oas["paths"][path][method]["parameters"].append({
                "name": name,
                "in": "path",
                "required": True,
                "description": f"Path parameter '{name}'.",
                "schema": schema
            })


    def document_query_parameter(self, query_parameter: str, path: str, method: str) -> None:
        """
        Documents a query parameter for a request. The path and method are used to locate where the query parameter should be documented.

        Args:
            query_parameter: The query parameter to document for the request.
            path: The path of the query parameter.
            method: The HTTP method of the query parameter.
        """

        if "=" in query_parameter:
            name, value = query_parameter.split("=", 1)
        else:
            name, value = query_parameter, None

        # if the query parameter already exists in the list of parameters, do not add it and return
        for parameter in self.oas["paths"][path][method]["parameters"]:
            if parameter["name"] == name and parameter["in"] == "query":
                return

        parameter_description = f"Query parameter '{name}'."

        if self.generate_descriptions:
            description_prompt = config.PROMPTS["query-parameter-description"].format(query_parameter=name,api_name=self.api_name, http_method=method.upper(), path=path)
            parameter_description = self.llm.prompt(description_prompt)

        # document the query parameter schema
        allow_empty_value = False
        schema = {
            "type": "string",
            "example": value
        }

        if value is None:
            allow_empty_value = True
            schema = {
                "type": "boolean"
            }
        elif value.isdigit():
            schema["type"] = "integer"

        self.oas["paths"][path][method]["parameters"].append({
            "name": name,
            "in": "query",
            "required": False,
            "description": parameter_description,
            "schema": schema,
            "allowEmptyValue": allow_empty_value
        })


    def save(self) -> None:
        """
        Saves the generated OAS documentation to a .json file.
        """

        out_path = config.OUT_PATH / self.api_id / "oas-documentation.json"

        utils.save_json(out_path, self.oas)