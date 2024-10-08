""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api/1.0/deals, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("1.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deals"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("storeID="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("title="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["batman"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("desc="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("price="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("upperPrice="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("lowerPrice="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sortBy="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["price"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageNumber="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("onSale="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("AAA="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("release="),
    primitives.restler_fuzzable_int("1", examples=["2022"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamRating="),
    primitives.restler_fuzzable_int("1", examples=["70"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("metacritic="),
    primitives.restler_fuzzable_int("1", examples=["75"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exact="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("cheaper="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamAppID="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.cheapshark.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/1.0/deals"
)
req_collection.add_request(request)

# Endpoint: /api/1.0/games, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("1.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("games"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("storeID="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("title="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["batman"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sortBy="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["price"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("desc="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exact="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamworks="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("onSale="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("AAA="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("metacritic="),
    primitives.restler_fuzzable_int("1", examples=["75"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageNumber="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamAppID="),
    primitives.restler_fuzzable_int("1", examples=["12345"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["price"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("lowerPrice="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("upperPrice="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamRating="),
    primitives.restler_fuzzable_int("1", examples=["90"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sortby="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["price"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("price="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("savings="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("releaseDate="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2022-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dealRating="),
    primitives.restler_fuzzable_int("1", examples=["80"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("isOnSale="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.cheapshark.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/1.0/games"
)
req_collection.add_request(request)

# Endpoint: /api/1.0/stores, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("1.0"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stores"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("storeID="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("title="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["batman"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageSize="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sortBy="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["name"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("desc="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("onSale="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamworks="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("AAA="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("metacritic="),
    primitives.restler_fuzzable_int("1", examples=["80"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("releaseDate="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2021-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("lowerPrice="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("upperPrice="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pageNumber="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ascending="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exact="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("steamAppID="),
    primitives.restler_fuzzable_int("1", examples=["570"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("storeId="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["price"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("activate="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.cheapshark.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/1.0/stores"
)
req_collection.add_request(request)
