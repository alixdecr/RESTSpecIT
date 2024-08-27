import json, os
from classes.api_inferer import ApiInferer


"""
Class which is used to test APIs by automating the inference process until no new elements from the documentation are found.
"""
class ApiTester:


    """
    Constructor function.
    """
    def __init__(self, config):

        self.config = config
        self.outPath = config["execution"]["out-path"]


    """
    Function which tests the benchmark APIs.
    PROCEDURE:
    - Iterate over a list of APIs given as input

    - For each API:
        - Find its corresponding documentation in the input folder
        - Create a file with the documented routes and parameters and set them to false
        - Add the API to an execution queue, with its remaning amount of retries

    - While APIs still have retries in the execution queue:
        - Iterate over the execution queue
        - Execute a test iteration for the API
        - Verify if the test yields new documentation features; If so, change values to true
        - If no new doc found, reduce retries by 1
        - If no more retries, remove API from queue as no more features were discovered
    """
    def execute(self, apiList):

        apiDict = {}

        for api in apiList:

            apiName = api.replace(" ", "_") # replace API name spaces with underscores
            # open the API doc
            with open(f"./inputs/docs/{apiName}_doc.json", "r") as openfile:
                doc = json.load(openfile)

            # create doc dict
            docDict = {"doc-routes": {"total": len(doc["documentation"]["routes"]), "found": 0, "names": {}}, "doc-parameters": {"total": len(doc["documentation"]["parameters"]), "found": 0, "names": {}}, "undoc-routes": {"total": 0, "list": []}, "undoc-parameters": {"total": 0, "list": []}, "other-routes": {"total": 0, "list": []}, "other-parameters": {"total": 0, "list": []}, "parameter-values": {}}

            # set routes to false
            for route in doc["documentation"]["routes"]:
                docDict["doc-routes"]["names"][route] = False

            # set parameters to false
            for parameter in doc["documentation"]["parameters"]:
                docDict["doc-parameters"]["names"][parameter] = False

            # create output api folder
            apiOutPath = f"{self.outPath}/{apiName}"
            # create output folders for the API
            folderList = [self.outPath, apiOutPath]
            for folder in folderList:
                if not os.path.exists(folder):
                    os.mkdir(folder)

            # save it to outputs
            self.saveDoc(docDict, apiOutPath)

            # create api dict
            apiDict[apiName] = {
                "name": api,
                "doc": docDict,
                "execId": 0,
                "retries": 2,
                "outPath": apiOutPath,
                "strategy": "focusAll"
            }

        remainsExec = True

        while remainsExec:

            remainsExec = False

            for api in apiDict:

                if apiDict[api]["retries"] > 0:

                    remainsExec = True

                    # update API exec ID
                    apiDict[api]["execId"] += 1

                    # set API related config
                    self.config["api"]["name"] = apiDict[api]["name"]
                    self.config["execution"]["out-path"] = apiDict[api]["outPath"]

                    # execute inferer for API
                    inferer = ApiInferer(self.config)
                    execData = inferer.execute(apiDict[api]["execId"], apiDict[api]["strategy"])

                    foundData = False

                    # when execution is finished, compare results
                    # routes
                    for route in execData["routes"]["list"]:
                        # if found route is documented, set doc value of route to true
                        if route in apiDict[api]["doc"]["doc-routes"]["names"]:
                            # if not already found
                            if apiDict[api]["doc"]["doc-routes"]["names"][route] == False:
                                apiDict[api]["doc"]["doc-routes"]["names"][route] = True
                                apiDict[api]["doc"]["doc-routes"]["found"] += 1
                                foundData = True

                        elif route not in apiDict[api]["doc"]["other-routes"]["list"]:
                            apiDict[api]["doc"]["other-routes"]["list"].append(route)
                            apiDict[api]["doc"]["other-routes"]["total"] += 1

                        # check if the doc contains an {id} field that might not necessarily be an integer
                        # find the position of the last "/"
                        lastPath = route.rfind("/")
                        # replace the substring after the last "/" with "{id}"
                        newRoute = route[:lastPath + 1] + "{id}"
                        # check
                        if newRoute in apiDict[api]["doc"]["doc-routes"]["names"]:
                            if apiDict[api]["doc"]["doc-routes"]["names"][newRoute] == False:
                                apiDict[api]["doc"]["doc-routes"]["names"][newRoute] = True
                                apiDict[api]["doc"]["doc-routes"]["found"] += 1
                                foundData = True

                    # parameters
                    for param in execData["parameters"]["list"]:
                        # if found parameter is documented, set doc value of param to true
                        if param in apiDict[api]["doc"]["doc-parameters"]["names"]:
                            # if not already found
                            if apiDict[api]["doc"]["doc-parameters"]["names"][param] == False:
                                apiDict[api]["doc"]["doc-parameters"]["names"][param] = True
                                apiDict[api]["doc"]["doc-parameters"]["found"] += 1
                                foundData = True
                        elif param not in apiDict[api]["doc"]["other-parameters"]["list"]:
                            apiDict[api]["doc"]["other-parameters"]["list"].append(param)
                            apiDict[api]["doc"]["other-parameters"]["total"] += 1

                    # values
                    for value in execData["parameter-values"]:
                        if value not in apiDict[api]["doc"]["parameter-values"]:
                            # set values
                            apiDict[api]["doc"]["parameter-values"][value] = execData["parameter-values"][value]
                        else:
                            for v in execData["parameter-values"][value]:
                                if v not in apiDict[api]["doc"]["parameter-values"][value]:
                                    apiDict[api]["doc"]["parameter-values"][value].append(v)

                    # save it to outputs
                    self.saveDoc(apiDict[api]["doc"], apiDict[api]["outPath"])

                    # if no data found, update retries
                    if not foundData:
                        apiDict[api]["retries"] -= 1
                    # if data was found, reset the retries index
                    else:
                        apiDict[api]["retries"] = 2

                    # if all routes and parameters of the API were found, set the retries to 0
                    if apiDict[api]["doc"]["doc-routes"]["found"] == apiDict[api]["doc"]["doc-routes"]["total"] and apiDict[api]["doc"]["doc-parameters"]["found"] == apiDict[api]["doc"]["doc-parameters"]["total"]:
                        apiDict[api]["retries"] = 0

                    # if all routes were found, only parameter mutations
                    elif apiDict[api]["doc"]["doc-routes"]["found"] == apiDict[api]["doc"]["doc-routes"]["total"]:
                        apiDict[api]["strategy"] = "focusParameters"

                    # if all parameters were found, only route mutations
                    elif apiDict[api]["doc"]["doc-parameters"]["found"] == apiDict[api]["doc"]["doc-parameters"]["total"]:
                        apiDict[api]["strategy"] = "focusRoutes"


    """
    Function which saves found documentation data to an external file.
    """
    def saveDoc(self, doc, outPath):

        # save it to outputs
        with open(f"{outPath}/found_doc.json", "w") as outfile:
            json.dump(doc, outfile, indent=4)