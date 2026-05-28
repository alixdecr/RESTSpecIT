from .BaseModel import BaseModel
from openai import OpenAI


class DeepSeekModel(BaseModel):


    def __init__(self, llm_id: str) -> None:
        """
        Initializes the DeepSeekModel class instance with the BaseModel class __init__.

        Args:
            llm_id: The identifier of the LLM to use.
        """

        super().__init__(llm_id)

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com",
            max_retries=3,
            timeout=10.0
        )


    def prompt_model(self, message: str) -> tuple[str | None, int, int]:
        """
        Prompts the model with a message.

        Args:
            message: The message to send to the LLM.

        Returns:
            A tuple containing the answer, the input tokens consumed, and the output tokens consumed.
        """

        response = self.client.chat.completions.create(
            model = self.llm_id,
            temperature = self.temperature,
            max_completion_tokens = self.max_tokens,
            messages = [{"role": "user", "content": message}],
            extra_body={"thinking": {"type": "disabled"}}
        )

        answer = response.choices[0].message.content
        nb_input_tokens = response.usage.prompt_tokens if response.usage else 0
        nb_output_tokens = response.usage.completion_tokens if response.usage else 0

        return answer, nb_input_tokens, nb_output_tokens