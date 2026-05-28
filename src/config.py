import logging
import time
import utils
from pathlib import Path


TIMESTAMP = time.strftime("%Y-%m-%d-%H-%M")

ROOT_PATH = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT_PATH / "config.json"
LOGS_PATH = ROOT_PATH / "logs"
OUT_PATH = ROOT_PATH / "outputs"
DATA_PATH = ROOT_PATH / "data"
PROMPTS_PATH = DATA_PATH / "prompts.json"
COMMON_PATHS_PATH = DATA_PATH / "common-paths.txt"
OAS_TEMPLATE_PATH = DATA_PATH / "oas-template.json"

LOGS_PATH.mkdir(parents=True, exist_ok=True)
OUT_PATH.mkdir(parents=True, exist_ok=True)

# setup logger configuration
logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="{asctime} | {levelname:<8} | {filename:<25} | {funcName:<25} | {lineno:<4} | {message}",
    style="{",
    handlers=[
        logging.FileHandler(LOGS_PATH / f"{TIMESTAMP}.log"),
        logging.StreamHandler()
    ]
)

PROMPTS = utils.load_json(PROMPTS_PATH)
EXECUTION = utils.load_json(CONFIG_PATH)
OAS_TEMPLATE = utils.load_json(OAS_TEMPLATE_PATH)
COMMON_PATHS = utils.load_txt_to_list(COMMON_PATHS_PATH)