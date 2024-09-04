import re, requests, time


"""
Function which makes a HTTP request and returns data related to the obtained response.
"""
def makeHTTPRequest(request, logger, apiKey="", method="get"):

    logger.logText(f"{request}", "request")

    # empty response by default
    responseData = {"request": request, "code": 0, "valid": True, "reason": "valid-req", "contentType": "", "text": "", "json": {}}

    # this function only supports get
    if method == "get":

        try:
            # if there is an Authorization header in the API key string, it should go in the headers of the request
            if "Authorization" in apiKey:
                # as apiKey contains the whole authorization header, only keep the API key for the Python requests header format
                header = {"Authorization": apiKey.replace(" ", "").split(":")[1]}
                response = requests.get(request, headers=header, timeout=10) # 10 second timeout by default

            else:
                # if there is an API key and that it contains an "=" character, the key is a query parameter
                if "=" in apiKey:
                    # the API key query parameter name is what is before the "="
                    apiKeyParam = apiKey.split("=")[0]

                    if apiKeyParam not in request:
                        if "?" in request:
                            request = request + f"&{apiKey}"
                        else:
                            request = request + f"?{apiKey}"
                    else:
                        pattern = rf"{apiKeyParam}=[^&]*"
                        request = re.sub(pattern, apiKey, request)

                response = requests.get(request, timeout=10) # 10 second timeout by default

            # check if response contains content type
            if "Content-Type" in response.headers:
                responseData["contentType"] = response.headers["Content-Type"]

            # check if response contains json
            if "application/json" in responseData["contentType"]:
                try:
                    responseData["json"] = response.json()
                except:
                    print("API response header 'Content-Type' specified 'application/json', but data is not parsable.")

            # check if response contains text 
            if ("text" in responseData["contentType"] or "json" in responseData["contentType"]) and response.text:
                responseData["text"] = response.text
                # search in the response data string if the "error" substring is present (case insensitive)
                # only check for "error", "not found" and "status" strings in small responses, as text or json error messages tend to be short
                if re.search(r"error|not found|status|invalid", response.text, re.IGNORECASE) and len(responseData["text"]) < 200:
                    responseData["valid"] = False
                    responseData["reason"] = "error-msg"

            else:
                responseData["text"] = "<" + responseData["contentType"] + " DATA>"

            # check status code
            responseData["code"] = response.status_code

            if responseData["code"] in range(400, 600):
                responseData["valid"] = False
                responseData["reason"] = "status-code"

        except:
            # if request failure, return a timeout error in data
            responseData = {"request": request, "code": 408, "valid": False, "reason": "timeout", "contentType": "", "text": "", "json": {}}

    # log response data
    logger.logRequest(responseData)

    if responseData["valid"]:
        logger.logText(f"Valid Request | Status Code: {responseData['code']}", "success")
    else:
        logger.logText(f"Invalid Request | Status Code: {responseData['code']} | Reason: {responseData['reason']}", "error")

    # if the responde status code is 429 (too many requests), sleep for 60 seconds
    if responseData["code"] == 429:
        logger.logText("Invalid Request | Status Code: 429 (Too Many Requests) - PAUSING EXECUTION FOR 30s", "error")
        time.sleep(30)

    return responseData