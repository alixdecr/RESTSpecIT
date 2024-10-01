""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("results="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("gender="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["male"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nat="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["us"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("inc="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["name,email"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exc="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["login"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("seed="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["abc123"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("password="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["upper"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["json"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: randomuser.me\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api"
)
req_collection.add_request(request)
