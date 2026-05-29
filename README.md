# RESTSpecIT: REST API Specification Inference Tool

![Version](https://img.shields.io/badge/Version-1.0.0-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Supported LLMs](https://img.shields.io/badge/Supported%20LLMs-GPT%%20%7C%20DeepSeek-purple)

Repository of the tool RESTSpecIT.

**Disclaimer 1: Please respect REST API rate limits when not using the tool locally, as lots of requests may be sent to API servers. The developers of the tool are not responsible for potential IP blacklists and/or API bans. The `wait-time-between-requests` configuration parameter may be used when executing the tool on online services.**

**Disclaimer 2: The tool utilizes LLMs for inference purposes. Be wary of (1) exposing your API key, and (2) exceeding your billing plans.**

## Installation

To install and use the tool, you can follow the instructions below. There are also helpful videos for the tool:
- Short demonstration: https://youtu.be/OM6Q4Le3kTM
- Full installation guide: https://youtu.be/jMGHEl0MO2M

### 1. Clone the Repository

First, clone the repository of the tool and navigate to it with:

```bash
git clone https://github.com/alixdecr/restspecit
cd <your-repository-folder>
```

### 2. Create a Virtual Environment

To use the tool, a Python virtual environment is recommended to avoid messing up your main Python interpreter. To do so, execute the following command in your repository folder:

```bash
python -m venv .venv
```

Which will create a Python virtual environment in the `.venv` folder. Depending on your Python installation and operation system, you might need to replace `python` with `py`, `python3`, or something else.

### 3. Activate the Virtual Environment

To activate the newly created virtual environment, execute the following command depending on your operating system:

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

##### CMD

```bash
.venv\Scripts\activate.bat
```

##### PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### 4. Install the Requirements

Before using the tool, you must upgrade pip and install the requirements using:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. LLM Setup

An LLM access key is required for the tool to send prompts and receive responses. To set it up, create a `.env` file at the root folder of the tool, and specify your LLM key as `LLM_API_KEY=<my-api-key>`. **Make sure to never share this file online to avoid exposing your LLM key.** `.env` is included in the `.gitignore` file to avoid accidents.

The tool currently supports GPT and DeepSeek models. To use other model families, please refer to the "LLM Support" section.

### 6. Execute the Tool

After installation, you can execute the tool with the following command:

```bash
python src/main.py
```

Once the tool terminates, outputs will be located in the `outputs/<api-name>` folder. There, you will find the generated OAS file, request seeds, and execution logs.

Steps 4 and 5 need to be done with the virtual environment activated (which should be the case if you followed step 3 correctly).

## Configuration File

It is possible to configure the tool's execution by modifying the `config.json` file. The following parameters may be set:

`apis`: A list of REST APIs to be inferred and documented by the tool. Each element of the list is structured as a JSON object, with the following sub-parameters:
- `name`: The name of the API.
- `base-url`: The base URL/endpoint of the API.
- `api-key`: An (optional) API key. If the API does not require a key, set the value to `null`.
- `wait-time-between-requests`: The time to wait in between requests, if the API has rate limiting. If the API does not limit requests, set the value to `0`.
- `documentation-baseline-path`: The path of a documentation baseline (for evaluation purposes). If the is no baseline, set the value to `null`.

`error-keyword-heuristic`: `true` if the error keyword heuristic should be used in the response oracle, `false` otherwise.

`generate-descriptions`: `true` if descriptions should be generated in the OAS file for the API, paths, query parameters, etc., `false` otherwise. The LLM is responsible for generating such descriptions.

`infer-common-paths`: `true` if common API paths should be inferred, `false` otherwise. The list of common paths is located in `data/common-paths.txt`.

`infer-keywords`: `true` if API keywords should be inferred, `false` otherwise.

`llm-id`: The identifier of the LLM to use.

`max-mutations`: The maximum number of mutations that the tool will apply (i.e., the mutation budget).

`methods-fallback`: A list of HTTP methods to be used as fallback, in case the OPTIONS method is not supported by the API.

`methods-to-check`: A list of HTTP methods that should be checked by the tool. For instance, if the list is `["get", "post"]` and a DELETE method is to be inferred, it will be skipped by the tool.

`same-response-heuristic`: `true` if the same response heuristic should be used in the response oracle, `false` otherwise.

## LLM Support

The tool supports GPT LLMs by default. However, adding support for other LLMs is very easy and straightforward:

1. Verify that the LLM has a Python library available for API calls.
2. Create a new class for your LLM that extends `BaseModel.py`. The template of the new LLM class should be structured as follows:

```python
from classes.BaseModel import BaseModel
# import your LLM Python library here

class NewModel(BaseModel):

    # provide the LLM ID to be used, such as 'gpt-4.1-mini'
    def __init__(self, llm_id):

        super().__init__(llm_id)

        # LLM-dependent setup goes here

    def prompt_model(self, message):

        # LLM-dependent response goes here
        response = ...

        # for the integration to work, the prompt_model function should return the LLM answer and the consumed input/output tokens
        answer = ...
        nb_input_tokens = ...
        nb_output_tokens = ...

        return answer, nb_input_tokens, nb_output_tokens
```

3. Update `main.py` by replacing the currently instantiated LLM with the new one.

Extending the `BaseModel` class correctly should allow you to use other LLMs without having to change any other part of the tool's code. However, if the LLM requires an API key to be used, do not forget to specify it.