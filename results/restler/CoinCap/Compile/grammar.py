""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /v2/assets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exchangeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/bitcoin, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("bitcoin"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["cardano"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/bitcoin"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/ethereum, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ethereum"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/ethereum"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/litecoin, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("litecoin"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("symbol="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["LTC"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minCap="),
    primitives.restler_fuzzable_int("1", examples=["1000000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxSupply="),
    primitives.restler_fuzzable_int("1", examples=["1000000000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["01/01/2019 00:00:00"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["01/02/2019 00:00:00"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/litecoin"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/cardano, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cardano"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/cardano"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/polkadot, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("polkadot"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["h1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["active"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("symbol="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["DOT"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rank="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minCap="),
    primitives.restler_fuzzable_int("1", examples=["100000000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxCap="),
    primitives.restler_fuzzable_int("1", examples=["1000000000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("changePercent="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1h"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/polkadot"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/stellar, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stellar"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("time="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("minSupply="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("maxSupply="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/stellar"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/chainlink, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("chainlink"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/chainlink"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/dogecoin, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dogecoin"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["marketCap"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["daily"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2022-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2022-12-31"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rank="),
    primitives.restler_fuzzable_int("1", examples=["100"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("symbol="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["DOGE"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["coin"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/dogecoin"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/eos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("eos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/eos"
)
req_collection.add_request(request)

# Endpoint: /v2/exchanges, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("exchanges"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["active"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["spot"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rank="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("country="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["US"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("volume="),
    primitives.restler_fuzzable_int("1", examples=["1000000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assets="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("id="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["coinbase"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("slug="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["kraken"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exchangeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/exchanges"
)
req_collection.add_request(request)

# Endpoint: /v2/markets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("markets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exchangeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/markets"
)
req_collection.add_request(request)

# Endpoint: /v2/rates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rates"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_int("1", examples=["0"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["asc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("symbol="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["BTC"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("rank="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exchangeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/rates"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/dogecoin/markets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dogecoin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("markets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2022-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1d"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("quote="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["BTC"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exchange="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("time="),
    primitives.restler_fuzzable_int("1", examples=["1609459200000"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["31/01/2022 23:59:59"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/dogecoin/markets"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/tron, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tron"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("offset="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2021-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2021-12-31"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/tron"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/tezos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tezos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/tezos"
)
req_collection.add_request(request)

# Endpoint: /v2/candles, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("candles"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("exchangeId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["binance"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["m1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["rank"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/candles"
)
req_collection.add_request(request)

# Endpoint: /v2/rates/:interval, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(":interval"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["bitcoin,ethereum"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/rates/:interval"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/ethereum/markets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ethereum"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("markets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/ethereum/markets"
)
req_collection.add_request(request)

# Endpoint: /v2/assets/ethereum/history, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ethereum"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("history"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("interval="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["d1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("convert="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["USD"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: api.coincap.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v2/assets/ethereum/history"
)
req_collection.add_request(request)
