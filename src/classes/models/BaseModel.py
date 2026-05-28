import logging
import os


logger = logging.getLogger(__name__)


class BaseModel:


    def __init__(self, llm_id: str) -> None:
        """
        Initializes the BaseModel class instance.

        Args:
            llm_id: The identifier of the LLM to use.
        """

        self.llm_id = llm_id
        self.api_key = os.getenv("LLM_API_KEY")
        self.temperature = 1
        self.max_tokens = 1000
        self.nb_prompts = 0
        self.tokens = {
            "input": 0,
            "output": 0
        }

        logger.info(f"Instantiated LLM: {self.llm_id}")


    def prompt(self, message: str, retries: int = 3) -> str | None:
        """
        Prompts the model with a message.

        Args:
            message: The message to send to the LLM.
            retries: The number of retries in case of an error.

        Returns:
            The response of the LLM for the prompt, or None if no response could be obtained.
        """

        logger.info(f"Sending prompt: {message}")

        answer = None

        while(retries > 0):
            retries -= 1
            self.nb_prompts += 1

            try:
                answer, nb_tokens_input, nb_tokens_output = self.prompt_model(message)
                self.add_tokens(nb_tokens_input, nb_tokens_output)
                retries = 0

                logger.info(f"LLM Responded: {answer}")

            except Exception as e:
                logger.error(f"LLM prompt error: {e}")

        return answer


    def add_tokens(self, nb_tokens_input: int, nb_tokens_output: int) -> None:
        """
        Adds a number of input and output tokens to their corresponding class attributes.

        Args:
            nb_tokens_input: The number of input tokens.
            nb_tokens_output: The number of output tokens.
        """

        self.tokens["input"] += nb_tokens_input
        self.tokens["output"] += nb_tokens_output


    def prompt_model(self, message: str) -> tuple[str | None, int, int]:

        return "Implement this function in the LLM model class.", 0, 0