import re


"""
Function which parses a given request URL string into a dictionary containing data related to the request.
"""
def requestToDict(request):

    requestExp = r"(?P<base>https?:\/\/[^\/\?]+)(?P<routes>\/[^?]*)?(?P<parameters>\?[^\/]+)?"
    requestDict = {}

    # remove all whitespaces
    request = request.replace(" ", "")

    parsedRequest = re.search(requestExp, request)

    # if the request has at least a base and a route expression (parameter group is optional), analyze it
    if parsedRequest:
        requestDict = {"base": parsedRequest.group("base"), "routes": {"unparsed": parsedRequest.group("routes"), "parsed": []}, "parameters": {"unparsed": parsedRequest.group("parameters"), "parsed": []}}

        # if the routes group is not None
        if requestDict["routes"]["unparsed"]:

            # if single "/", remove it as it is not required
            if requestDict["routes"]["unparsed"] == "/":
                requestDict["routes"]["unparsed"] = ""

            else:
                # check if last element is a '/'
                if requestDict["routes"]["unparsed"][-1] == "/":
                    requestDict["routes"]["unparsed"] = requestDict["routes"]["unparsed"][:-1]
                # parse all the paths by removing their '/' and only keeping their names
                routeList = requestDict["routes"]["unparsed"].split("/")
                # remove empty routes
                for r in routeList:
                    if r == "":
                        routeList.remove(r)
                
                requestDict["routes"]["parsed"] = routeList

        else:
            requestDict["routes"]["unparsed"] = ""

        # if the parameter group is not None
        if requestDict["parameters"]["unparsed"]:

            # remove '?' and separate by '&'
            parameterList = requestDict["parameters"]["unparsed"].replace("?", "").split("&")
            
            for parameter in parameterList:
                # split by name and value
                data = parameter.split("=")

                # if the parameter has no value, set it to None
                if len(data) < 2:
                    data.append(None)

                requestDict["parameters"]["parsed"].append({"name": data[0], "value": data[1]})

        else:
            requestDict["parameters"]["unparsed"] = ""

    return requestDict


"""
Function which parses a given request dictionary into a request URL string.
"""
def dictToRequest(dict):

    # start with the base
    request = dict["base"]

    # routes
    for route in dict["routes"]["parsed"]:
        request += "/" + route

    # parameters
    if len(dict["parameters"]["parsed"]) > 0:
        # '?' indicates start of parameters
        request += "?"

        for index in range(len(dict["parameters"]["parsed"])):
            parameter = dict["parameters"]["parsed"][index]

            request += parameter["name"]
            # if the parameter has a value, add it
            if parameter["value"] != None:
                request += "=" + parameter["value"]

            # if there are still parameters next in the list, add a '&' separator
            if index < len(dict["parameters"]["parsed"]) - 1:
                request += "&"

    return request