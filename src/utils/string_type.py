import ast


"""
Function which returns the type of the given string (evaluated literally) in the OpenAPI format.
"""
def getStringType(string):

    # value is of type string by default
    data = {"type": "string"}

    try:
        value = ast.literal_eval(string)

    except:
        value = string

    data["type"] = type(value).__name__

    # convert types to OpenAPI types
    if data["type"] == "str":
        data["type"] = "string"

    elif data["type"] in ("list", "tuple"):
        data["type"] = "array"

    elif data["type"] == "float":
        data["type"] = "number"
        data["format"] = "float"

    elif data["type"] == "int":
        data["type"] = "integer"
        data["format"] = "int32"

    else:
        data["type"] = "object"

    # extra check for boolean values
    if string in ("True", "true", "False", "false"):
        data["type"] = "boolean"

    return data