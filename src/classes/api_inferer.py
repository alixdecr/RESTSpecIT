import json, os, random, re, time
from classes.api_llm import ApiLLM
from classes.api_mutator import ApiMutator
from classes.api_verifier import ApiVerifier
from classes.logger import Logger
from utils.find_regex import findEmail, findUrl
from utils.make_request import makeHTTPRequest
from utils.request_format import requestToDict
from utils.string_type import getStringType


"""
Class which is used to infer API specifications by generating/mutating requests and making LLM prompts.
"""
class ApiInferer:


    """
    Constructor function.
    """
    def __init__(self, config):

        # parameters
        self.apiName = config["api"]["name"]
        self.apiKey = config["api"]["key"]
        self.apiKeyParam = config["api"]["key-param"]
        self.rateLimit = config["api"]["rate-limit"]
        self.excludeRoutes = config["api"]["exclude-routes"]
        self.outPath = config["execution"]["out-path"]
        self.prompts = config["execution"]["prompts"]
        self.seedChoice = config["execution"]["seed-choice"] # random-route or random-seed
        self.local = config["api"]["local"]
        self.localUrl = config["api"]["local-url"]
        self.requestVerif = config["api"]["request-verif"]
        self.acceptHtml = config["api"]["accept-html"]

        # if the "outputs" folder does not exist yet, create the folder and its sub-folders
        folderList = [self.outPath, f"{self.outPath}/seeds", f"{self.outPath}/logs", f"{self.outPath}/executions"]
        for folder in folderList:
            if not os.path.exists(folder):
                os.mkdir(folder)

        # define output paths
        self.openapiPath = f"{self.outPath}/openapi.json"
        self.validSeedsPath = f"{self.outPath}/seeds/valid_seeds.txt"
        self.invalidSeedsPath = f"{self.outPath}/seeds/invalid_seeds.txt"

        # setup API data
        self.apiData = {}
        self.seedList = []
        self.invalidSeedList = []

        # data which keeps track of requests and what was discovered
        self.executionData = {"requests": {"valid": 0, "total": 0}, "routes": {"amount": 0, "list": []}, "parameters": {"amount": 0, "list": []}, "parameter-values": {}, "strategies": [], "time": 0, "tokens": {"input": 0, "output": 0}}

        # API classes
        self.logger = Logger(config)
        self.llm = ApiLLM(config, self.logger)
        self.verifier = ApiVerifier(config, self.logger)
        self.mutator = ApiMutator(config, self.llm, self.logger)
        

    """
    Function which executes the inference process.
    """
    def execute(self, execId, strategy="focusAll"):

        executionPath = f"{self.outPath}/executions/{execId}.json"

        # print tool and api name
        self.logger.logMessage("RESTSpecIT: The RESTful API Specification Inference Tool, powered with GPT", "title", "blue", True)
        self.logger.logMessage(f"Executing for: {self.apiName}", "title", "blue", True)

        # start time
        startTime = time.time()

        # load existing API data or create new API data 
        self.loadApiData()
        self.loadApiSeeds("valid")
        self.loadApiSeeds("invalid")

        # base data
        self.findBaseData()

        # mutation process
        if strategy == "focusAll":
            self.mutateRequests(1, "focusRoutes")
            self.mutateRequests(1, "focusParameters")

        else:
            self.mutateRequests(1, strategy)

        # end time
        endTime = time.time()

        # results
        self.logger.logMessage("Execution Results", "title", "blue", True)
        self.logger.logMessage("Saved to", "bullet", "purple", True, executionPath)

        # add time to exec data
        self.executionData["time"] = f"{str(round(endTime - startTime, 2))}s"

        # add token count to exec data
        self.executionData["tokens"] = self.llm.tokens

        # save exec data to file
        with open(executionPath, "w") as outfile:
            json.dump(self.executionData, outfile, indent=4)

        return self.executionData


    """
    Function which will make LLM prompts in order to find the base data of the API, and save this data to an external file.
    """
    def findBaseData(self):

        self.logger.logMessage("Inferring Base API Data", "title", "blue", True)

        # INFO DATA
        self.logger.logMessage("Info Data...", "arrow", "blue", True)

        if self.apiData["info"]["title"] == "":
            # API description
            descPrompt = f"Return a very short description of the '{self.apiName}'."
            descResponse = self.llm.makeLLMRequest(descPrompt)

            # terms of service URL
            termsPrompt = f"Return the terms of service URL of the '{self.apiName}'. You must only reply with the URL."
            termsUrl = self.llm.promptUrl(termsPrompt)

            # contact URL
            contactPrompt = f"Return the 'contact us' or 'support' URL of the '{self.apiName}'. You must only reply with the URL."
            contactUrl = self.llm.promptUrl(contactPrompt)

            # email
            emailPrompt = f"Return the e-mail address used to contact the '{self.apiName}'. You must only reply with the e-mail address."
            emailResponse = self.llm.makeLLMRequest(emailPrompt)
            emailString = findEmail(emailResponse)

            # license name
            licensePrompt = f"Return the name of the license used by the '{self.apiName}'. You must only reply with the name of the license and nothing else."
            licenseResponse = self.llm.makeLLMRequest(licensePrompt)

            # license URL
            licenseUrlPrompt = f"Return the URL of the '{licenseResponse}' license. You must only reply with the URL."
            licenseUrl = self.llm.promptUrl(licenseUrlPrompt)

            # add the generated description to the default description
            descString = self.apiData["info"]["description"] + descResponse

            self.apiData["info"] = {
                "title": self.apiName,
                "description": descString,
                "termsOfService": termsUrl,
                "contact": {
                    "name": f"{self.apiName} Contact",
                    "url": contactUrl,
                    "email": emailString
                },
                "license": {
                    "name": licenseResponse,
                    "url": licenseUrl
                },
                "version": "v1"
            }
            self.logger.logMessage("Info Data Found", "arrow", "green")
            self.saveApiData()

        else:
            self.logger.logMessage("Info Data Already Exists", "arrow", "yellow")

        # EXTERNAL DOC DATA
        self.logger.logMessage("External Doc Data...", "arrow", "blue", True)

        if self.apiData["externalDocs"]["url"] == "":
            # documentation
            docPrompt = f"Return the documentation URL for requests to the '{self.apiName}'. You must only reply with the URL."
            docUrl = self.llm.promptUrl(docPrompt)

            self.apiData["externalDocs"] = {
                "url": docUrl,
                "description": f"Find more about the {self.apiName} here:"
            }
            self.logger.logMessage("External Doc Data Found", "arrow", "green")
            self.saveApiData()

        else:
            self.logger.logMessage("External Doc Data Already Exists", "arrow", "yellow")

        # SERVER DATA
        self.logger.logMessage("Server Data...", "arrow", "blue", True)

        if self.apiData["servers"][0]["url"] == "":
            # base URL
            basePrompt = f"Return the base URL for requests to the '{self.apiName}'. You must only reply with the URL."
            response = self.llm.makeLLMRequest(basePrompt)
            baseUrl = findUrl(response)

            # find nb of base routes
            nbBase = 0
            if baseUrl != "":
                requestDict = requestToDict(baseUrl)
                baseUrl = requestDict["base"]
                nbBase = len(requestDict["routes"]["parsed"])

            self.apiData["servers"] = [{
                "url": baseUrl,
                "description": f"Production Server of the {self.apiName}.",
                "x-base-routes": nbBase
            }]

            self.logger.logMessage("Server Data Found", "arrow", "green")
            self.saveApiData()

        else:
            self.logger.logMessage("Server Data Already Exists", "arrow", "yellow")

        # VALID REQUEST SEED
        self.logger.logMessage("Valid Request Seed...", "arrow", "blue", True)

        # for local APIs
        if self.local:

            self.apiData["servers"] = [{
                "url": self.localUrl,
                "description": f"Local Production Server of the {self.apiName}.",
                "x-base-routes": self.localUrl.count("/")
            }]

            self.seedList = [self.localUrl]
            responseData = {
                            "request": self.seedList[0],
                            "code": 200,
                            "valid": True,
                            "reason": "valid-req",
                            "contentType": "application/json",
                            "text": "Valid request",
                            "json": {"valid": "true", "response": "this is a valid request"}
                        }
            # log response data
            self.logger.logRequest(responseData)
            self.inferRequest(self.seedList[0], responseData)

        if len(self.seedList) <= 0:
            # seed URL
            seedPrompt = f"Return an example of a complete and valid HTTP request URL that can be made to the '{self.apiName}'. If the request allows query parameters, add some to the end of the URL. You must only reply with the URL."

            seedUrl = self.llm.promptUrl(seedPrompt, True, self.apiKeyParam, self.apiKey)

            if seedUrl != "":

                responseData = makeHTTPRequest(seedUrl, self.logger)

                if responseData["valid"]:

                    # find nb of base routes based on exclude-routes config
                    if self.apiData["servers"][0]["x-base-routes"] == 0:
                        requestDict = requestToDict(seedUrl)
                        nbBase = 0
                        for i in requestDict["routes"]["parsed"]:
                            # lowercase to match patterns such as api, Api, v1, V1, etc.
                            i = i.lower()
                            if i in self.excludeRoutes:
                                # add 1 to the nb of base routes and add path to server URL
                                nbBase += 1
                            # break to prevent base routes discontinuity
                            else:
                                break

                        self.apiData["servers"][0]["x-base-routes"] = nbBase

                    self.logger.logMessage("Valid Request Seed Found", "arrow", "green")
                    self.inferRequest(seedUrl, responseData)
                else:
                    self.logger.logMessage("Valid Request Seed Not Found", "arrow", "red")
            else:
                self.logger.logMessage("Valid Request Seed Not Found", "arrow", "red")
        
        else:
            self.logger.logMessage("Valid Request Seed Already Exists", "arrow", "yellow")

         # set nb base routes for the mutator
        self.mutator.apiNbBase = self.apiData["servers"][0]["x-base-routes"]

        # ERROR SCHEMA
        self.logger.logMessage("Error Schema...", "arrow", "blue", True)

        # if server url exists, use it as a base
        if self.apiData["servers"][0]["url"] != "":
            self.verifier.inferErrorSchema(self.apiData["servers"][0]["url"])

        # else use seed
        elif len(self.seedList) > 0:
            self.verifier.inferErrorSchema(self.seedList[0])

        self.apiData["components"]["schemas"]["ErrorSchema"] = self.verifier.errorSchema
        self.logger.logMessage("Error Schema Found", "arrow", "green")

        self.saveApiData()


    """
    Function which choses, mutates and verifies requests based on the mutation strategy specified as parameter.
    """
    def mutateRequests(self, iterations, strategy):

        # add strategy to recap
        self.executionData["strategies"].append(strategy)

        self.logger.logMessage(f"Mutation Process - Strategy: {strategy}", "title", "blue", True)

        if len(self.seedList) == 0:
            self.logger.logMessage(f"Cannot mutate as no seeds exist", "arrow", "red", True)

        else:
            # for each iteration, chose a seed and apply all mutation operators onto it in order to find mutated requests
            for i in range(iterations):
                self.logger.logMessage(f"Mutating Request ({i + 1}/{iterations})", "title", "blue", True)

                # apply mutation strategy
                mutatedList = self.mutator.applyStrategy(strategy, self.seedList, list(self.apiData["paths"].keys()))

                self.logger.logMessage("Mutated Request Verification", "title", "blue", True)

                for request in mutatedList:
                    # if API request rate limiting, sleep x seconds
                    if self.rateLimit > 0:
                        time.sleep(self.rateLimit)

                    self.logger.logMessage("Request", "bullet", "purple", True, request)

                    # if the API requires a key, add it
                    if self.apiKey != "" and f"{self.apiKeyParam}={self.apiKey}" not in request:
                        if "?" in request:
                            request = request + f"&{self.apiKeyParam}={self.apiKey}"
                        else:
                            request = request + f"?{self.apiKeyParam}={self.apiKey}"

                    # if there is not request verification
                    if not self.requestVerif:
                        responseData = {
                            "request": request,
                            "code": 200,
                            "valid": True,
                            "reason": "valid-req",
                            "contentType": "application/json",
                            "text": "Valid request",
                            "json": {"valid": "true", "response": "this is a valid request"}
                        }
                        # log response data
                        self.logger.logRequest(responseData)

                    else:
                        responseData = makeHTTPRequest(request, self.logger)

                    self.executionData["requests"]["total"] += 1

                    # if the request is valid
                    if responseData["valid"]:
                        # flag out HTML (or not if accept-html parameter is true) as it indicates a web page and not data as response (json, text, image, etc.)
                        if "html" not in responseData["contentType"] or self.acceptHtml:
                            self.logger.logMessage("Valid Request", "arrow", "green", True)
                            self.inferRequest(request, responseData)
                            self.executionData["requests"]["valid"] += 1
                        else:
                            self.logger.logMessage("Invalid Request - Response is of HTML format", "arrow", "yellow", True)
                    else:
                        self.logger.logMessage(f"Invalid Request due to '{responseData['reason']}'", "arrow", "red", True)

                        if request not in self.invalidSeedList:
                            self.saveApiSeed(request, "invalid")
        

    """
    Function which infers the API OpenAPI specification based on a given valid request and its response data.
    """
    def inferRequest(self, request, responseData):

        # put the request in dict form
        requestDict = requestToDict(request)

        # add valid request to seeds if not in it yet
        if request not in self.seedList:
            self.seedList.append(request)
            self.saveApiSeed(request)

        else:
            self.logger.logMessage(f"Request already exists in seeds", "arrow", "yellow", True)

        if requestDict != {}:

            # if a path of the route is an integer, change it to {id} as it represents an ID value
            route = ""
            # start from the route after the base routes
            for index in range(len(requestDict["routes"]["parsed"])):
                path = requestDict["routes"]["parsed"][index]
                if path.isdigit():
                    path = "{id}"
                route += "/" + path

            parameters = requestDict["parameters"]["parsed"]

            # add route to execution recap
            if route not in self.executionData["routes"]["list"]:
                self.executionData["routes"]["amount"] += 1
                self.executionData["routes"]["list"].append(route)

            # if the route is not in the data yet, create a new object for it
            if route not in self.apiData["paths"]:

                if self.prompts["routeDesc"]:
                    # route description
                    routePrompt = f"Return a very short description of the '{route}' route from the '{self.apiName}' API."
                    routeResponse = self.llm.makeLLMRequest(routePrompt)

                    # route response description
                    routeRespPrompt = f"Return a very short description of what a request to the '{route}' route from the '{self.apiName}' API returns as data."
                    routeRespResponse = self.llm.makeLLMRequest(routeRespPrompt)

                else:
                    routeResponse = "No description."
                    routeRespResponse = "No description."

                # replace '/' with '_' for schema ID and remove semicolons as they are not standard
                routeSchema = "ResponseSchema" + route.replace("/", "_").replace("{","").replace("}", "")

                # add path parameter if '{id}' in route
                defaultParams = []
                if "{id}" in route:
                    data = {
                        "name": "id",
                        "description": f"ID path parameter for the {route} route.",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                            "format": "int32"
                        }
                    }
                    defaultParams.append(data)

                # create a new route data in the OpenAPI format
                self.apiData["paths"][route] = {
                    "get": {
                        "description": routeResponse,
                        "parameters": defaultParams,
                        "responses": {
                            "200": {
                                "description": routeRespResponse,
                                "content": {
                                    f"{responseData['contentType']}": {
                                        "schema": {
                                            "$ref": f"#/components/schemas/{routeSchema}"
                                        },
                                        "example": responseData["json"] if responseData["json"] != {} else (responseData["text"] if len(responseData["text"]) < 400 else responseData["text"][:400] + "...")
                                    }
                                }
                            },
                            "default": self.verifier.errorDefault
                        }
                    }
                }
                # add schema too
                self.apiData["components"]["schemas"][f"{routeSchema}"] = {}

            # parameter data
            if len(parameters) > 0:

                for index in range(len(parameters)):

                    parameter = parameters[index]

                    # add parameter to execution recap
                    if parameter["name"] not in self.executionData["parameters"]["list"]:
                        self.executionData["parameters"]["amount"] += 1
                        self.executionData["parameters"]["list"].append(parameter["name"])
                        # setup parameter value list
                        self.executionData["parameter-values"][parameter["name"]] = [parameter["value"]]
                    else:
                        if parameter["value"] not in self.executionData["parameter-values"][parameter["name"]]:
                            self.executionData["parameter-values"][parameter["name"]].append(parameter["value"])
                    
                    # get the parameter index in the list (if not in the list, will get the value None) if the parameter is a query parameter and not a path parameter
                    paramIndex = next((p for p, item in enumerate(self.apiData["paths"][route]["get"]["parameters"]) if (item["name"] == parameter["name"] and item["in"] == "query")), None)

                    # if the parameter is not in the path
                    if paramIndex == None:

                        if parameter["value"] != None:
                            paramData = getStringType(parameter["value"])

                            # set example value
                            examples = {f"{parameter['value']}": {"value": parameter["value"]}}

                            # if the type is boolean, value can only be true or false
                            if paramData["type"] == "boolean":
                                examples = {
                                    "true": {
                                        "value": "true"
                                    },
                                    "false": {
                                        "value": "false"
                                    }
                                }
                        
                        # if the parameter has no value, set its type to 'x-null'
                        else:
                            paramData = {"type": "x-null"}
                            examples = {}

                        # get parameter description
                        name = parameter["name"]

                        if self.prompts["parameterDesc"]:
                            paramPrompt = f"Return a very short description of the '{name}' parameter from the '{self.apiName}' API."
                            paramResponse = self.llm.makeLLMRequest(paramPrompt)
                        else:
                            paramResponse = "No description."

                        # add parameter to data
                        parameterData = {
                            "name": name,
                            "description": paramResponse,
                            "in": "query",
                            "required": False,
                            "schema": paramData,
                            "examples": examples
                        }
                        # add the new parameter to the parameter list
                        self.apiData["paths"][route]["get"]["parameters"].append(parameterData)

                        # set the parameter index to the length of the list as it was appended last
                        paramIndex = len(self.apiData["paths"][route]["get"]["parameters"]) - 1

                    # get parameter value after creating it or retrieving it
                    paramItem = self.apiData["paths"][route]["get"]["parameters"][paramIndex]

                    # check if parameter value does not exist, if parameters examples < 10
                    if parameter["value"] != None and parameter["value"] not in paramItem["examples"] and len(paramItem["examples"]) < 10:
                        # add value to dict
                        paramItem["examples"][parameter["value"]] = {
                            "value": parameter["value"]
                        }

                        # if old parameter type is "x-null", change it
                        if paramItem["schema"]["type"] == "x-null":
                            paramItem["schema"] = getStringType(parameter["value"])

        self.saveApiData()


    """
    Function which loads API data from an external file. If no external file exists, will load default data.
    """
    def loadApiData(self):

        # if the file already exists, load it
        if os.path.isfile(self.openapiPath):
            filePath = self.openapiPath
            self.logger.logMessage("Loaded API Data", "arrow", "green", True)

        else:
            # by default, the file to load is the default openapi data
            filePath = "./src/utils/default_openapi.json"
            self.logger.logMessage("Created New API Data File", "arrow", "green", True)

        # load file data
        with open(filePath, "r", encoding="utf-8") as openfile:
            self.apiData = json.load(openfile)



    """
    Function which saves API data to an external file.
    """
    def saveApiData(self):

        # save data to file
        with open(self.openapiPath, "w", encoding="utf-8") as outfile:
            json.dump(self.apiData, outfile, indent=4)
            self.logger.logMessage("Saved API Data", "arrow", "green", True)


    """
    Function which loads API seeds from an external file. If no external file exists, load empty list
    """
    def loadApiSeeds(self, seedType="valid"):

        path = self.validSeedsPath

        if seedType == "invalid":
            path = self.invalidSeedsPath

        # if the file already exists, load it
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as openfile:
                if seedType == "valid":
                    self.seedList = openfile.read().splitlines()
                else:
                    self.invalidSeedList = openfile.read().splitlines()

                self.logger.logMessage("Loaded API Seeds", "arrow", "green", True)

        else:
            self.logger.logMessage("Created New API Seed File", "arrow", "green", True)


    """
    Function which saves an API seed to an external file.
    """
    def saveApiSeed(self, seed, seedType="valid"):

        path = self.validSeedsPath

        if seedType == "invalid":
            path = self.invalidSeedsPath

        # add to seed file
        with open(path, "a", encoding="utf-8") as outfile:
            outfile.write(f"{seed}\n")

            if seedType == "valid":
                self.logger.logMessage("Saved API Seed", "arrow", "green", True)