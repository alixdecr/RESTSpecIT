""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api/activity, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("activity"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("participants="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["education"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("price="),
    primitives.restler_fuzzable_number("1.23", examples=["0.5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("accessibility="),
    primitives.restler_fuzzable_number("1.23", examples=["0.1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minaccessibility="),
    primitives.restler_fuzzable_number("1.23", examples=["0.2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxparticipants="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minprice="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxprice="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minparticipants="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxaccessibility="),
    primitives.restler_fuzzable_number("1.23", examples=["0.5"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.boredapi.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/activity"
)
req_collection.add_request(request)

# Endpoint: /api, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("participants="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("accessibility="),
    primitives.restler_fuzzable_number("1.23", examples=["0.1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["diy"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.boredapi.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api"
)
req_collection.add_request(request)
