import time
from openai import OpenAI
from utils.find_regex import findUrl
from utils.make_request import makeHTTPRequest


"""
Class which is used to setup OpenAI information and make model prompts.
"""
class ApiLLM():


    """
    Constructor function.
    """
    def __init__(self, config, logger):

        self.openaiKey = config["llm"]["openai-key"]
        self.temperature = config["llm"]["temperature"]
        self.model = config["llm"]["model"]
        self.logger = logger

        # token usage tracker
        self.tokens = {"input": 0, "output": 0}

        # setup OpenAI key
        self.client = OpenAI(
            api_key=self.openaiKey
        )


    """
    Function which makes a request to the OpenAI API. Retries 10 times by default in case of a model error.
    """
    def makeLLMRequest(self, text, retries=10):

        promptData = {"prompt": text, "response": "", "object": None}
        retryIndex = 0

        while retryIndex < retries:
            retryIndex += 1

            try:
                request = self.client.chat.completions.create(
                    model = self.model,
                    temperature = self.temperature,
                    max_tokens = 1000,
                    messages = [
                        {"role": "user", "content": text}
                    ],
                    timeout = 10 # 10 second timeout in case the LLM request freezes
                )

                promptData["object"] = request
                promptData["response"] = request.choices[0].message.content
                retryIndex = retries
                # add tokens
                self.addTokens(request.usage)
            
            # in case of a timeout error, set response as empty string
            except Exception as e:
                self.logger.logText(f"Invalid LLM Prompt Request: {e} - PAUSING EXECUTION FOR 5s", "error")
                promptData["response"] = ""
                time.sleep(5)

            # log prompt data
            self.logger.logPrompt(promptData)

        return promptData["response"]
    

    """
    Function which prompts the LLM for a URL and verifies its validity. If the URL is invalid, will re-prompt the model a certain amount of times for a valid one.
    """
    def promptUrl(self, prompt, apiRequest=False, apiKey="", retries=3):

        retryIndex = 0
        oldPrompt = prompt

        while retryIndex < retries:
            retryIndex += 1
            response = self.makeLLMRequest(prompt)
            url = findUrl(response)

            if url != "":

                validityData = makeHTTPRequest(url, self.logger, apiKey=apiKey)

                # if the url is valid, set the retry index to the number of retries to exit the while loop
                # if API request, response data has to be valid
                # if URL, only status code has to be valid
                if (apiRequest and validityData["valid"]) or (not apiRequest and validityData["code"] in range(200, 300)):
                    retryIndex = retries

                # else change the prompt and put url as empty string
                else:
                    url = ""
                    prompt = f"The following URL you returned is invalid: '{validityData['request']}'. Retry the following by returning a different URL: '{oldPrompt}'"

        return url
    

    """
    Function which adds the input and output tokens of an OpenAI API prompt to a dictionary.
    """
    def addTokens(self, tokens):

        self.tokens["input"] += tokens.prompt_tokens
        self.tokens["output"] += tokens.completion_tokens