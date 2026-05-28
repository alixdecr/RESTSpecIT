import config
import logging
from classes.Crawler import Crawler
from classes.models.DeepSeekModel import DeepSeekModel
from dotenv import load_dotenv


logger = logging.getLogger(__name__)
load_dotenv()


def main() -> None:
    """
    Main function for the program execution.
    """

    if "llm-id" not in config.EXECUTION:
        logger.warning("Cannot execute: Missing llm-id field in config.json")
        return

    llm_id = config.EXECUTION.get("llm-id", "deepseek-v4-flash") # defaults to deepseek-v4-flash if no model is found in the config file
    api_configs = config.EXECUTION.get("apis", [])

    for api_config in api_configs:
        llm = DeepSeekModel(llm_id)
        crawler = Crawler(llm, api_config)
        crawler.execute()


if __name__ == "__main__":
    main()