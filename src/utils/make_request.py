import re, requests, time


"""
Function which makes a HTTP request and returns data related to the obtained response.
"""
def makeHTTPRequest(request, logger, method="get"):

    # empty response by default
    responseData = {"request": request, "code": 0, "valid": True, "reason": "valid-req", "contentType": "", "text": "", "json": {}}

    # this function only supports get
    if method == "get":

        try:
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

    return responseData