from utils.make_request import makeHTTPRequest
from utils.request_format import requestToDict
from utils.string_type import getStringType


"""
Class which is used to verify API responses based on the behavior of the API.
"""
class ApiVerifier:


    """
    Constructor function.
    """
    def __init__(self, config, logger):

        # parameters
        self.apiName = config["api"]["name"]
        self.logger = logger

        # OpenAPI data schema for an error
        self.errorSchema =  {}

        # OpenAPI default for error
        self.errorDefault = {
            "description": "Request Error",
            "content": {}
        }


    """
    Function which infers the error schema of an API by voluntarily generating and sending an invalid request to the API endpoint.
    """
    def inferErrorSchema(self, validRequest):

        requestDict = requestToDict(validRequest)

        invalidRequest = requestDict["base"] + requestDict["routes"]["unparsed"] + "/invalidRoute/?invalidParam=invalidValue" # add an additional fake route

        responseData = makeHTTPRequest(invalidRequest, self.logger)

        # based on the response data of an error, find error schema
        if responseData["json"] != {}:
            keyList = list(responseData["json"].keys())

            self.errorSchema = {
                "type": "object",
                "properties": {},
                "required": keyList
            }

            for key in keyList:
                self.errorSchema["properties"][key] = getStringType(responseData["json"][key])

        # if response data of an error is not json, do not make a schema for it
        else:
            self.errorSchema["type"] = "string"

        # default error
        self.errorDefault["content"][responseData["contentType"]] = {
            "schema": {
                "$ref": "#/components/schemas/ErrorSchema"
            },
            "example": responseData["json"] if responseData["json"] != {} else (responseData["text"] if len(responseData["text"]) < 400 else (responseData["text"][:400] + "..."))
        }