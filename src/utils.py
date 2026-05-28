import json
import logging
import re
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


def get_canonical_url(url: str, include_query: bool = True) -> str:
    """
    Constructs the canonical URL for a given URL.
    The function does so by (1) replacing path parameters with placeholders (digits, files, country codes, UUIDs, API versions), and (2) sorting query parameters by alphabetical order.
    For instance, if the URL is "/v1.3/pets/3/food?id=3&adopted=1", the corresponding canonical URL would be "/{version}/pets/{digits}/food?adopted={value}&id={value}"

    Args:
        url: The URL to convert to canonical form.
        include_query: True if the query should be included, False otherwise.

    Returns:
        The canonical URL.
    """

    COUNTRY_CODE_MATCH = re.compile(r"^[A-Z]{2}$")
    FILE_MATCH = re.compile(r"^[A-Za-z0-9_-]+\.(?:pdf|txt|csv|json|xml|zip|png|jpe?g)$")
    UUID_MATCH = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
    VERSION_MATCH = re.compile(r"^(?:v\d(?:\.\d)?)|(?:\d\.\d)$")

    # separate path and query
    if "?" in url:
        path, query = url.split("?", 1)
    else:
        path = url
        query = ""

    # normalize paths
    paths = []

    for part in path.split("/"):

        # match path parameter with digits
        if part.isdigit():
            paths.append("{digits}")

        # match path parameter with file
        elif FILE_MATCH.match(part):
            ext = part.split(".", 1)[1]
            paths.append(f"{{file}}.{ext}")

        # match path parameter with country code
        elif COUNTRY_CODE_MATCH.match(part):
            paths.append("{country-code}")

        # match path parameter with UUID
        elif UUID_MATCH.match(part):
            paths.append("{uuid}")

        # match path parameter with version
        elif VERSION_MATCH.match(part):
            paths.append("{version}")

        else:
            paths.append(part)

    canonical_path = "/".join(paths)

    # normalize query
    parameters = []

    if query and include_query:
        for parameter in query.split("&"):
            if "=" in parameter:
                key = parameter.split("=")[0]
                value = "{value}"
            else:
                key = parameter
                value = None

            parameters.append((key, value))

        parameters.sort(key=lambda x: x[0])

    # rebuild query
    canonical_query = "&".join(
        f"{key}={value}" if value else key
        for key, value in parameters
    )

    # construct canonical URL
    if canonical_query:
        return f"{canonical_path}?{canonical_query}"
    
    return canonical_path


def get_url_query_parameters(url: str) -> list[tuple[str, str]]:
    """
    Retrieves a list of query parameters (or query parameter names) from a given URL string.
    The list is given as tuples of key, value pairs.

    Args:
        url: The URL string.
        names_only: True if only the query parameter names should be retrieved, False otherwise.

    Returns:
        The list of query parameter tuples (key, value).
    """

    url = url.strip()

    if "?" not in url:
        return []
    
    query = url.split("?", 1)[1]

    if not query:
        return []
    
    split_query = query.strip().split("&")
    query_params = []
    seen = []

    for param in split_query:
        if not param:
            continue

        if "=" in param:
            key, value = param.split("=", 1)
        else:
            key, value = param, ""

        key = param.split("=", 1)[0]
        value = None

        if "=" in param:
            value = param.split("=", 1)[1]

        # to avoid duplicates
        if not key or key in seen:
            continue

        query_params.append((key, value))
        seen.append(key)

    return query_params
    

def json_to_str(json_data: dict[Any, Any]) -> str:
    """
    Converts JSON data into a string.
    
    Args:
        json_data: The JSON data in a dictionary.

    Returns:
        A string of the JSON data. The string is empty if an error occurred.
    """

    try:
        return json.dumps(json_data)

    except Exception as e:
        logger.error(f"Unexpected error while converting json to str: {e}")
        return ""


def load_json(path: Path) -> dict[Any, Any]:
    """
    Loads JSON data from a path in a dictionary.
    
    Args:
        path: The path of the JSON data.

    Returns:
        A dictionary containing the loaded JSON data. The dictionary is empty if an error occurred.
    """

    if not path.exists():
        logger.warning(f"JSON file not found: {path}")
        return {}

    try:
        with path.open("r", encoding="utf-8") as file:
            json_content = json.load(file)
            logger.info(f"Loaded JSON content from: {path}")
            return json_content
        
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON file {path}: {e}")
        return {}
        
    except Exception as e:
        logger.error(f"Unexpected error loading JSON file {path}: {e}")
        return {}


def load_txt_to_list(path: Path) -> list[str]:
    """
    Loads the content of a text file into a list (separated by newlines).

    Args:
        path: The path of the text file.
    
    Returns:
        A list containing each line of the text file. The list is empty if the path does not exist or if an error occurred.
    """

    if not path.exists():
        logger.warning(f"Text file not found: {path}")
        return []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            txt_content = [line.strip() for line in file]
            logger.info(f"Loaded text content from: {path}")
            return txt_content
        
    except Exception as e:
        logger.error(f"Unexpected error loading text file {path}: {e}")
        return []
    

def str_to_pascal_case(str: str) -> str:
    """
    Converts a path such as '/test/users' or '/api/v1/items' into PascalCase such as 'TestUsers' or 'ApiV1Items'.

    Args:
        str: The string to convert to PascalCase.

    Returns:
        The string converted to PascalCase.
    """

    parts = str.strip("/").split("/")
    return "".join(part.capitalize() for part in parts)
    

def save_json(path: Path, data: dict[Any, Any] | list[Any]) -> None:
    """
    Saves JSON data to a path.

    Args:
        path: The path where the JSON data will be saved.
        data: The JSON data as a dictionary to be saved.
    """

    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logger.info(f"Saved JSON file to: {path}")
    

def str_to_json(str: str) -> dict[Any, Any]:
    """
    Converts a string into JSON data.
    
    Args:
        str: The string to convert.

    Returns:
        A dictionary of the JSON data extracted from the string. The dictionary is empty if an error occurred.
    """

    try:
        return json.loads(str)

    except Exception as e:
        logger.error(f"Unexpected error while converting str to json: {e}")
        return {}