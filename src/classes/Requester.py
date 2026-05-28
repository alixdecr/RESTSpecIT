import config
import logging
import requests
from .Dataclasses import Validity
from typing import Any


logger = logging.getLogger(__name__)


class Requester:


    def __init__(self) -> None:
        """
        Initializes the Requester class instance.
        This class is used to handle sending requests and receiving responses from REST API servers.
        """

        self.nb_requests = 0


    def check_response(self, response: requests.Response, old_response: requests.Response | None = None) -> Validity:
        """
        Executes the oracle to assess the validity of the HTTP request's response.
        The error keyword heuristic will check for false positives in 2xx-3xx responses, by verifying if the response content only contains error-related keywords (e.g., "error", "not found", etc.).

        Args:
            response: The response to analyze.
            old_response: An optional old response to compare the current response with. If both responses are identical, the function will flag the current response as invalid.

        Returns:
            The validity of the response represented by valid/invalid and a message.
        """
        
        error_keyword_heuristic = config.EXECUTION.get("error-keyword-heuristic", True)
        same_response_heuristic = config.EXECUTION.get("same-response-heuristic", True)
        status_code = response.status_code
        content = response.text.lower().strip()

        validity = Validity("valid", "valid request", status_code)

        if 400 <= status_code < 500:
            validity.category = "invalid"
            validity.message = "client error"

        elif 500 <= status_code < 600:
            validity.category = "invalid"
            validity.message = "server error"

        elif error_keyword_heuristic and 200 <= status_code < 400 and (content == "error" or content == "not found"):
            validity.category = "invalid"
            validity.message = "false positive"
        
        elif same_response_heuristic and old_response and self.is_identical_responses(response, old_response):
            validity.category = "invalid"
            validity.message = "identical responses"

        logger.info(f"Oracle flagged response as '{validity.category}' due to '{validity.message}'")

        return validity


    def get_url_methods(self, url: str) -> list[str]:
        """
        Retrieves all HTTP method supported by the given URL, by verifying the presence/content of the "Allow" response header.

        Args:
            url: The URL to analyze.

        Returns:
            A list of HTTP methods supported by the URL. The list is empty if no method was found or if an error occurred.
        """

        logger.info(f"Finding HTTP methods for: {url}")
        response = self.send_request(url, "options")

        if response is None:
            return []
        
        try:
            allow_header = response.headers.get("Allow")

            if allow_header is None:
                logger.warning(f"Unsupported 'Allow' header for: {url}")
                return []

            methods = [method.strip().lower() for method in allow_header.split(",")]
            logger.info(f"Found HTTP methods for {url}: {str(methods)}")
            return methods

        except Exception as e:
            logger.error(f"Unexpected error while trying to find HTTP methods for {url}: {e}")
            return []
        

    def is_identical_responses(self, response_1: requests.Response, response_2: requests.Response) -> bool:
        """
        Checks if the content of 2 HTTP responses are identical.

        Args:
            response_1: The first response to analyze.
            response_2: The second response to analyze.

        Returns:
            True if the responses are identical, False otherwise.
        """

        response_1_str = response_1.text
        response_2_str = response_2.text

        return response_1_str == response_2_str


    def send_request(self, url: str, method: str, payload: dict[Any, Any] | None = None, timeout: int = 10) -> requests.Response | None:
        """
        Sends a request (HTTP method and URL, with an optional payload) and returns its response.
        
        Args:
            url: The URL of the request.
            method: The HTTP method of the request.
            payload: An optional payload for the request.
            timeout: The time to wait before timing out the request.

        Returns:
            The response of the request, or None if an error occurred.
        """

        method_uppercase = method.upper()
        logger.info(f"Sending request: '{method_uppercase} {url}'")

        try:
            response = requests.request(
                method=method,
                url=url,
                json=payload,
                timeout=timeout
            )

            self.nb_requests += 1
            status_code = response.status_code
            logger.info(f"Received response for '{method_uppercase} {url}': {status_code}")
            return response

        except requests.exceptions.RequestException as e:
            logger.error(f"Request error while sending request '{method_uppercase} {url}': {e}")
            return None

        except Exception as e:
            logger.error(f"Unexpected error while sending request '{method_uppercase} {url}': {e}")
            return None