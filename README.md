# RESTSpecIT
![alt text](https://img.shields.io/badge/Version-1.0-orange.svg) ![alt text](https://img.shields.io/badge/LLM-GPT--3.5_|_GPT--4-purple.svg) ![alt text](https://img.shields.io/badge/Minimal_User_Input-API_Name,_OpenAI_Key-brightgreen.svg)  [![alt text](https://img.shields.io/badge/LinkedIn-blue.svg)](https://www.linkedin.com/in/alix-decrop)

## Introduction

This repository contains the replication package for the tool RESTSpecIT (RESTful API Specification Inference and Testing). In all, the following can be found:

- The source code of RESTSpecIT, in the `/src` folder.

- The evaluation results of RESTSpecIT, in the `/evaluation-results` folder. Inside, each output corresponds to a separate execution of the tool with all 10 benchmark APIs.

- The evaluation results of RESTSpecIT outputs as RESTler inputs, in the `/restler-evaluation-results` folder.

- The inputs required by RESTSpecIT, in the `/inputs` folder. This folder contains the configuration file for the user, and the documentation used during the evaluation of the benchmark APIs.

The tool was designed by Alix Decrop, for the research paper "You Can REST Now: Automated Specification Inference and Black-Box Testing of RESTful APIs with Large Language Models". The paper can be found [here](https://arxiv.org/abs/2402.05102).

## Prerequisites

1. A Python installation, with version 3.11.5 or higher. The `py --version` command displays the version of Python installed on the machine.

2. The package manager pip, with version 23.3.1 or higher. The `pip --version` command displays the version of pip installed on the machine.

3. An OpenAI key, which can be generated at the following URL: https://platform.openai.com/account/api-keys

4. A minimal amount ($5) of OpenAI credit, required to use the GPT-3.5 model through the OpenAI API. Even though RESTSpecIT costs $0.008 on average for a RESTful API execution, OpenAI imposes this minimum amount for unrestricted access to the model.

## Using the Tool

1. Download the replication package. If the download is a .zip file, extract the content of the file in a directory of your choice.

2. Once downloaded, open a command prompt and type in the following command: `cd PATH_TO_REPLICATION_PACKAGE`. The path corresponds to the location where the replication package was downloaded.

3. If this is the first time using the tool, the following Python packages need to be installed: `[colorama, openai, requests]`. Download the required Python packages by typing `py -m pip install -r pip-requirements.txt`. Depending on your machine and Python version, `py` may need to be replaced with `python`, `python3` or else.

4. Outside of the command prompt and in the root folder of the replication package, a configuration file can be found in `/inputs/config.json`. Make sure that **all** fields (except `key` and `key-param` if the API does not require an authentication key) are correctly filled in. To use the tool with the default settings, only fill in the `name` and `openai-key` fields. If the API imposes a rate limit, do not forget to include a number of seconds to wait between requests in the `rate-limit` field.

4. Return to the command prompt previously opened, and type in `py ./src/main.py` to launch the tool.

## Configuration Parameters

- `api.name: string` - The name of the RESTful API to execute. The name should be followed by `API`, such as `PetStore API`.

- `api.key: string` - The authentication string with the key used to access the API. If the API does not require a key, leave the value as an empty string. If the API requires the key in a query parameter, write it (e.g. `apiKey=XXXXX`). If the API requires the key in a header field, write the header field (e.g. `Authorization: XXXXX`). The tool will automatically detect if the string should go in the request URL or in the request headers.

- `api.rate-limit: integer >= 0` - The amount of seconds to wait between requests sent to the API. This is useful if the API has a strict rate limiting. If no rate limiting is required, leave the value to 0.

- `api.exclude-routes: list[string]` - The names of the routes that will be excluded during the mutation process of the tool. This is used to avoid mutating base routes of the API. By default, `api, v1, v2, v3` are excluded as they are frequently API base route names.

- `api.local: boolean` - If the API is local (i.e. running on localhost).

- `api.local-url: string` - The URL of the local API. If the API is not local, insert an empty string.

- `api.request-verif: boolean` - If the generated requests should be verified w.r.t. the API server responses.

- `api.accept-html: boolean` - If a HTML response returned by the API should be considered as a valid response.

- `llm.openai-key: string` - The authentication key used to access the utilized Large Language Model API. For now, only OpenAI keys are supported.

- `llm.model: string` - The name of the Large Language Model used by the tool (`gpt-3.5-turbo` by default). For now, only GPT-3.5 and GPT-4 models are supported.

- `llm.temperature: float >= 0 and <= 2` - The randomness of model responses (`0.7` by default). Lower values make the model deterministic and repetitive, while higher values make the model more random. **Values above 1 are not recommended**.

- `execution.mode: string` - The execution mode of the tool. `infer` mode is default and recommended, as it executes the tool solely based on the API name. `test` mode utilizes the documentation from the `inputs` folder to compare RESTSpecIT results with existing API documentation.

- `execution.out-path: string` - The path where the outputs of the tool will be saved (`./outputs` by default).

- `execution.prompts.extraBaseData: boolean` - `true` if the tool should attempt to infer base API data (external documentation URL, API license, contact page, etc.), `false` otherwise.

- `execution.prompts.routeDesc: boolean` - `true` if the tool should generate OpenAPI human-readable descriptions for routes, `false` otherwise.

- `execution.prompts.parameterDesc: boolean` - `true` if the tool should generate OpenAPI human-readable descriptions for query parameters, `false` otherwise.

- `execution.max-route-query: integer >= 0 and <= 10` - The number of routes in each mutation where the tool will also prompt the model for additional query parameters related to the routes (`3` by default). This is useful for APIs that contain routes with mandatory query parameters.

- `execution.seed-init: string` - The strategy that the tool will employ to initialize the seed list (`all-routes-request` by default).
    - `single-seed`: Will only generate a single request seed.
    - `all-routes-seed`: Will generate a request seed for each route of the API found by the LLM.

- `execution.seed-choice: string` - The strategy that the tool will employ to select seeds (`random-route` by default).
    - `random-seed` (not recommended): Selects a random seed from the list of seeds.
    - `random-route` (recommended): Selects a random route from the list of routes that were found by the tool, and then selects a random seed that contains the randomly chosen route. This allows all discovered routes to be selected more evenly.