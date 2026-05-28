import utils
from pathlib import Path
from typing import Any


class Baseliner:


    def __init__(self, api_config: dict[Any, Any]) -> None:
        """
        Initializes the Baseliner class instance.
        This class is used for evaluation purposes.

        Args:
            api_config: The configuration of the API.
        """

        self.baseline = self.setup(api_config)


    def check(self, url: str, http_method: str) -> None:
        """
        Checks valid URL data and updates the found elements of the baseline accordingly.

        Args:
            url: The URL to analyze.
            http_method: The HTTP method to analyze.
        """

        if not self.baseline:
            return
        
        # convert to canonical URL
        url = utils.get_canonical_url(url)
        
        # routes
        try:
            path = "/" + url.split("://", 1)[1].split("?", 1)[0].split("/", 1)[1]
        except:
            path = "/"

        route = f"{http_method.upper()} {path}"

        if route not in self.baseline["routes"]["elements"] and route not in self.baseline["routes"]["undocumented-valid"]:
            self.baseline["routes"]["undocumented-valid"].append(route)

        if route in self.baseline["routes"]["elements"] and self.baseline["routes"]["elements"][route] is False:
            self.baseline["routes"]["elements"][route] = True
            self.baseline["routes"]["found"] += 1

        # query parameters
        if "?" in url:
            query = url.split("?", 1)[1]

            for parameter in query.split("&"):
                parameter_name = parameter.split("=", 1)[0]

                if parameter_name not in self.baseline["query-parameters"]["elements"] and parameter_name not in self.baseline["query-parameters"]["undocumented-valid"]:
                    self.baseline["query-parameters"]["undocumented-valid"].append(parameter_name)

                if parameter_name in self.baseline["query-parameters"]["elements"] and self.baseline["query-parameters"]["elements"][parameter_name] is False:
                    self.baseline["query-parameters"]["elements"][parameter_name] = True
                    self.baseline["query-parameters"]["found"] += 1


    def setup(self, api_config: dict[Any, Any]) -> dict[Any, Any] | None:
        """
        Setups up the documentation baseline for execution.
        This is for testing purposes, to verify how many documented elements were found by the tool.

        Args:
            api_config: The configuration parameters for the API.

        Returns:
            A dictionary with the baseline documentation information if there is a documentation baseline path in the API config, None otherwise.
        """

        baseline_path = api_config.get("documentation-baseline-path")

        if baseline_path is None:
            return None

        baseline_file = utils.load_json(Path(baseline_path))
        routes = baseline_file.get("routes", [])
        query_parameters = baseline_file.get("query-parameters", [])

        baseline = {
            "routes": {
                "total": len(routes),
                "found": 0,
                "elements": {},
                "undocumented-valid": []
            },
            "query-parameters": {
                "total": len(query_parameters),
                "found": 0,
                "elements": {},
                "undocumented-valid": []
            }
        }

        for route in routes:
            baseline["routes"]["elements"][route] = False

        for query_parameter in query_parameters:
            baseline["query-parameters"]["elements"][query_parameter] = False

        return baseline