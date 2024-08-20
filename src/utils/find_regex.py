import re


"""
Function which returns a string (from a given string) matching the given regex. Returns an empty string if the regex is not matched.
"""
def findRegex(string, exp):

    if re.search(exp, string):
        return re.findall(exp, string)[0]
    
    return ""


"""
Function which returns a URL string (from a given string) matching the given URL regex. Returns an empty string if the URL regex is not matched.
"""
def findUrl(string):

    if re.search(r"https?:\/\/[^\s]+", string):

        url = re.findall(r"https?:\/\/[^\s]+", string)[0]

        # remove parsing error and route delimitator
        if "'." in url:
            url = url.replace("'.", "")

        if url[-1] in ("'", "/", "."):
            url = url[:-1]

        return url
    
    return ""


"""
Function which returns a email string (from a given string) matching the given email regex. Returns an empty string if the email regex is not matched.
"""
def findEmail(string):

    if re.search(r"[^@]+@[^\.]+\.[a-z]{2,4}", string):
        return re.findall(r"[^@]+@[^\.]+\.[a-z]{2,4}", string)[0]
    
    return ""