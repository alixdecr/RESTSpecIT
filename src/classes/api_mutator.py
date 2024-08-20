import ast, random, re
from utils.request_format import dictToRequest, requestToDict


"""
Class which is used to mutate API requests.
"""
class ApiMutator:


    """
    Constructor function.
    """
    def __init__(self, config, llm, logger):

        # parameters
        self.apiName = config["api"]["name"]
        self.maxRouteQuery = config["execution"]["max-route-query"]
        self.seedChoice = config["execution"]["seed-choice"]
        self.llm = llm
        self.logger = logger
        self.apiNbBase = 0

        # mutation operators
        self.mutationOperators = {
            "addRoute": {"element": "route", "action": "add", "token": "<route>"},
            "removeRoute": {"element": "route", "action": "remove", "token": "<route>"},
            "modifyRoute": {"element": "route", "action": "modify", "token": "<route>"},
            "resetRoutes": {"element": "route", "action": "reset", "token": "<route>"},
            "addParameter": {"element": "query parameter", "action": "add", "token": "<parameter=value>"},
            "removeParameter": {"element": "query parameter", "action": "remove", "token": "<parameter=value>"},
            "modifyParameter": {"element": "query parameter", "action": "modify", "token": "<parameter=value>"},
            "resetParameters":{"element": "query parameter", "action": "reset", "token": "<parameter=value>"}
        }

        # optional mutation operators:
        # "modifyParameterName": {"element": "query parameter name", "action": "modify", "token": "<parameter>"},
        # "modifyParameterValue": {"element": "query parameter value", "action": "modify", "token": "<value>"},


    """
    Function which applies a mutation strategy by applying the related mutation operators individually.
    """
    def applyStrategy(self, strategy, seedList, routeList):

        chosenOperators = self.mutationOperators

        if strategy == "focusRoutes":
            chosenOperators = ["addRoute", "removeRoute", "modifyRoute", "resetRoutes"]
        
        elif strategy == "focusParameters":
            chosenOperators = ["addParameter", "removeParameter", "modifyParameter", "resetParameters"]

        mutatedRequests = []

        for operator in chosenOperators:
            seed = self.selectSeed(seedList, routeList)
            mutatedRequests = mutatedRequests + self.applyMutationOperator(seed, operator)

        return mutatedRequests


    """
    Function which applies a random mutation operator.
    """
    def applyRandomMutationOperator(self, request):

        return self.applyMutationOperator(request, random.choice(list(self.mutationOperators.keys())))


    """
    Function which applies a mutation operator.
    """
    def applyMutationOperator(self, request, mutationOperator):

        self.logger.logMessage("Mutation Operator", "bullet", "purple", True, mutationOperator)

        mutatedRequests = []
        requestDict = requestToDict(request)

        # check if mutation operator can be applied
        if mutationOperator not in ("removeRoute", "modifyRoute", "resetRoutes") or len(requestDict["routes"]["parsed"]) > self.apiNbBase:

            # mask request based on the operator
            maskedRequest = self.maskRequest(request, mutationOperator)

            self.logger.logMessage("Masked Request", "bullet", "purple", True, maskedRequest)

            # check if operator is not of type remove and if the masked request contains a placeholder token, starting with '<'
            if "remove" not in mutationOperator and "<" in maskedRequest:
                # generate prompt
                prompt = self.generatePrompt(maskedRequest, mutationOperator)

                # response
                response = self.llm.makeLLMRequest(prompt)

                # check if response is a list
                try:
                    # remove line breaks and multiple spaces
                    response = " ".join(response.split())
                    # find the list in the response if not returned directly by the model
                    response = re.findall(r"\[.+\]", response)[0]
                    # parse the string list
                    valueList = ast.literal_eval(response)
                except:
                    valueList = []
                    self.logger.logMessage("Invalid Prompt Response", "arrow", "red", True)

                # parse the values of the list
                if len(valueList) > 0:
                    valueList = self.parseValues(valueList, mutationOperator)

                # if modifying or adding a route
                if mutationOperator in ("addRoute", "modifyRoute", "resetRoutes"):

                    # add cases where route might need query parameters
                    if len(valueList) > 0:
                        for route in valueList:
                            if valueList.index(route) < self.maxRouteQuery:
                                # if route already contains a query, remove it
                                route = route.split("?")[0]
                                # replace <route> token with value
                                request = maskedRequest.replace(self.mutationOperators[mutationOperator]["token"], route)
                                reqDict = requestToDict(request)
                                routeReq = reqDict["base"] + reqDict["routes"]["unparsed"]

                                queryResponse = self.llm.makeLLMRequest(f"Return an example of a valid query that can be added at the end of the '/{route}' route in the following HTTP request: '{routeReq}'. You must only reply with a string of the query and no other text.")
                                # if space in value, replace it with a '+'
                                queryResponse = str(queryResponse).replace(" ", "+")
                                # if query is correctly returned
                                if re.search(r"\?[^\/\?]+", queryResponse):
                                    query = re.findall(r"\?[^\/\?]+", queryResponse)[0]
                                    valueList.append(route + query)

                    # add a random value between 1 and 100 that checks for a possible ID path as these are frequent in APIs and sometimes ignored by the LLM
                    randId = str(random.randint(1, 100))
                    valueList.append(randId)

                self.logger.logMessage("Found Values", "bullet", "purple", True, valueList)

                # for each value, find the corresponding mutated request by replacing the mask with the value
                for value in valueList:

                    # local masked request to avoid modifying the original
                    maskedRequestL = maskedRequest

                    # if value already contains a query, set the '?' in the request to a '&'
                    if '?' in value:
                        maskedRequestL = maskedRequestL.replace("?", "&")

                    # replace <op> token with value and cast value to string
                    request = maskedRequestL.replace(self.mutationOperators[mutationOperator]["token"], value)

                    mutatedRequests.append(request)

            else:
                mutatedRequests.append(maskedRequest)

        else:
            self.logger.logMessage("Cannot Apply Mutation Operator", "arrow", "red", True)

        return mutatedRequests


    """
    Function which returns a masked request based on a given request and a mutation operator.
    """
    def maskRequest(self, request, mutationOperator, keepParameters=True, index=-1):

        maskedRequest = ""
        requestDict = requestToDict(request)

        # ROUTE MUTATION OPERATORS

        if mutationOperator == "addRoute":
            # add <op> to the route list
            requestDict["routes"]["parsed"].append("<route>")

        elif mutationOperator == "removeRoute":
            # if there is at least a route
            if len(requestDict["routes"]["parsed"]) > 0:
                # remove last route of the route list
                del requestDict["routes"]["parsed"][index]

        elif mutationOperator == "modifyRoute":
            # replace the last route of the route list with <op>
            requestDict["routes"]["parsed"][index] = "<route>"

        elif mutationOperator == "resetRoutes":
            # reset the routes and add a single <op> (keep the routes until base routes of the API)
            requestDict["routes"]["parsed"] = requestDict["routes"]["parsed"][0:self.apiNbBase]
            requestDict["routes"]["parsed"].append("<route>")

        # PARAMETER MUTATION OPERATORS

        elif mutationOperator == "addParameter":
            # add a new parameter name <op> with value <op>
            requestDict["parameters"]["parsed"].append({"name": "<parameter", "value": "value>"})

        elif mutationOperator == "removeParameter":
            # if there is at least one parameter
            if len(requestDict["parameters"]["parsed"]) > 0:
                # remove the parameter with the specified index
                del requestDict["parameters"]["parsed"][index]

        elif mutationOperator == "modifyParameter":
            if len(requestDict["parameters"]["parsed"]) > 0:
                # change existing parameter with <op>
                requestDict["parameters"]["parsed"][index] = {"name": "<parameter", "value": "value>"}

        elif mutationOperator == "modifyParameterName":
            if len(requestDict["parameters"]["parsed"]) > 0:
                # change existing parameter name with <op>
                requestDict["parameters"]["parsed"][index] = {"name": "<parameter>", "value": requestDict["parameters"]["parsed"][index]["value"]}

        elif mutationOperator == "modifyParameterValue":
            if len(requestDict["parameters"]["parsed"]) > 0:
                # change existing parameter value with <op>
                requestDict["parameters"]["parsed"][index] = {"name": requestDict["parameters"]["parsed"][index]["name"], "value": "<value>"}

        elif mutationOperator == "resetParameters":
            # remove all but one parameter <op>
            requestDict["parameters"]["parsed"] = [{"name": "<parameter", "value": "value>"}]

        # if parameters should not be kept when mutating routes, remove them
        if mutationOperator in ["addRoute", "removeRoute", "modifyRoute", "resetRoutes"] and not keepParameters:
            requestDict["parameters"] = {"unparsed": "", "parsed": []}

        # reassemble the request from the mutated dict
        maskedRequest = dictToRequest(requestDict)

        return maskedRequest


    """
    Return a prompt for the model based on the mutation operator.
    """
    def generatePrompt(self, maskedRequest, mutationOperator):

        element = self.mutationOperators[mutationOperator]["element"]
        token = self.mutationOperators[mutationOperator]["token"]

        prompt = f"Return a Python list containing up to 10 different examples of distinct {element}s that can replace '{token}' in the following HTTP request to the '{self.apiName}': '{maskedRequest}'. You must only reply with the Python list containing {element}s." # To add with GPT4: The response should only contain the list without formatted Python code.

        return prompt
    

    """
    Parse the values returned by the model based on the mutation operator.
    """
    def parseValues(self, valueList, mutationOperator):

        parsedList = []
        element = self.mutationOperators[mutationOperator]["element"]

        for value in valueList:
            # if value is not an empty string
            if value != "":
                # cast to string and if space in value, replace it with a '+'
                value = str(value).replace(" ", "+")

                # if the model returns values between semicolons or other delimiters, it is mostly placeholder values to change with real values
                phExp = r"(({|<)[^}>]+(}|>))"
                if re.search(phExp, value):
                    placeholders = re.findall(phExp, value)
                    for p in placeholders:
                        value = value.replace(p[0], str(random.randint(1, 100)))

                # routes
                if element == "route":
                    # check if the route does not start with a '/' as it is already placed in the request
                    if value[0] == "/":
                        value = value[1:]
                    else:
                        value = value

                # parameters
                elif element == "query parameter" and re.search(r"[^\=\?\&\/]+=?[^\=\?\&\/]+", value):
                    value = re.findall(r"[^\=\?\&\/]+=?[^\=\?\&\/]+", value)[0]

                # parameter names and values
                elif element in ("query parameter name", "query parameter value") and re.search(r"[^\=\?\&\/]+", value):
                    value = re.findall(r"[^\=\?\&\/]+", value)[0]

                # if no matches, remove parameter
                else:
                    value = ""

                # if value is not an empty string and not already in the list
                if value != "" and value not in parsedList:
                    parsedList.append(value)

        return parsedList
    

    """
    Selects a request seed for mutation based on the given configuration.
    """
    def selectSeed(self, seedList, routeList):

        # random-route case
        if self.seedChoice == "random-route":
            randRoute = random.choice(routeList)

            # build route regex, in case a route containing '{id}' is chosen
            filterExp = ""
            pathList = randRoute.split("/")
            for p in pathList:
                if p == "{id}":
                    filterExp += "/" + r"\d+"

                elif p != "":
                    filterExp += "/" + p

            # filter seeds with the same route path
            filteredSeeds = []
            for s in seedList:
                if re.search(filterExp, s):
                    filteredSeeds.append(s)

            if len(filteredSeeds) > 0:
                # chose random from filtered
                seed = random.choice(filteredSeeds)
            
            # if no needs were filtered, chose random
            else:
                seed = random.choice(seedList)

        # random-seed case
        else:
            seed = random.choice(seedList)

        self.logger.logMessage("Chosen Seed", "bullet", "purple", True, seed)

        return seed