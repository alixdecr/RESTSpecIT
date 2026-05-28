import config
import logging
import utils
from dataclasses import asdict
from .Dataclasses import Validity, Variant, Seed
from typing import Any


logger = logging.getLogger(__name__)


class Seeder:


    def __init__(self, api_id: str) -> None:
        """
        Initializes the Seeder class instance.
        This class is used to handle the generated request seeds.

        Args:
            api_id: The identifier of the API.
        """

        self.seeds: list[Seed] = []
        self.out_path = config.OUT_PATH / api_id / "seeds.json"


    def add_seed(self, url: str, http_method: str, validity: Validity, payload: dict[Any, Any] | None = None) -> None:
        """
        Adds a given request to the list of seeds.

        Args:
            url: The URL of the seed.
            http_method: The HTTP method of the seed.
            validity: The validity of the seed.
            payload: The payload of the seed or None if the seed does not have one.
        """

        canonical_path = utils.get_canonical_url(url, include_query=False)
        canonical_url = utils.get_canonical_url(url)

        for seed in self.seeds:
            # if the seed exists
            if canonical_path == seed.canonical_path and http_method == seed.http_method:
                # check if an identical variant already exists
                for variant in seed.variants:
                    if canonical_url == variant.canonical_url:
                        return

                # if no identical variant was found, create it
                variant = Variant(canonical_url, url, payload, validity)
                seed.variants.append(variant)
                logger.info(f"Updated seed '{http_method.upper()} {canonical_path}' with variant '{url}' of category '{validity.category}'")
                return

        # if the seed does not exist yet, create it
        seed = Seed(canonical_path, http_method)
        variant = Variant(canonical_url, url, payload, validity)
        seed.variants.append(variant)
        self.seeds.append(seed)
        logger.info(f"Created seed '{http_method.upper()} {canonical_path}' with variant '{url}' of category '{validity.category}'")

        
    def exists_in_seeds(self, url: str, http_method: str, only_path: bool = False) -> bool:
        """
        Determines if a given request already exists in the seed list.

        Args:
            url: The URL to check.
            http_method: The HTTP method to check.
            only_path: True if the check should only be done at the canonical path level, False otherwise.

        Returns:
            True if the request exists in the seed list, False otherwise.
        """

        canonical_path = utils.get_canonical_url(url, include_query=False)
        canonical_url = utils.get_canonical_url(url)

        for seed in self.seeds:
            # if the seed exists
            if canonical_path == seed.canonical_path and http_method == seed.http_method:
                # if only checking for the canonical path existence, return true without checking the variants
                if only_path:
                    return True
                # check if the variant already exists
                for variant in seed.variants:
                    if canonical_url == variant.canonical_url:
                        return True
                    
        return False
    

    def only_invalid(self) -> bool:
        """
        Determines if there are only invalid seeds in the seed list.

        Returns:
            True if there are only invalid seeds, False otherwise.
        """

        for seed in self.seeds:
            for variant in seed.variants:
                if variant.validity.category == "valid":
                    return False
                
        return True


    def save(self) -> None:
        """
        Saves the seeds to an external file.
        """

        serialized_seeds = []

        for seed in self.seeds:
            serialized_seeds.append(asdict(seed))

        utils.save_json(self.out_path, serialized_seeds)