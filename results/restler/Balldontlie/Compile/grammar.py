""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api/v1/players, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("players"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["points"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/players"
)
req_collection.add_request(request)

# Endpoint: /api/v1/players/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("players"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("seasons[]="),
    primitives.restler_fuzzable_int("1", examples=["2019"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["desc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fields[]="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["id"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/players/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/teams, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1", examples=["10"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["points"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("conference="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["east"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("division="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["atlantic"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("city="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["toronto"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("abbreviation="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["LAL"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("full_name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Chicago+Bulls"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Warriors"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("year_founded="),
    primitives.restler_fuzzable_int("1", examples=["1995"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("venue="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Staples+Center"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/teams"
)
req_collection.add_request(request)

# Endpoint: /api/v1/games, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("games"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["5"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("seasons[]="),
    primitives.restler_fuzzable_int("1", examples=["2021"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start_date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2022-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end_date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2022-01-31"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("seasons="),
    primitives.restler_fuzzable_int("1", examples=["2020"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("dates="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2021-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("teams[]="),
    primitives.restler_fuzzable_int("1", examples=["1"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("players[]="),
    primitives.restler_fuzzable_int("1", examples=["23"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1", examples=["50"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["desc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["1,2,3"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("player_ids="),
    primitives.restler_fuzzable_int("1", examples=["12345"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("postseason="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("venue="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["home"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/games"
)
req_collection.add_request(request)

# Endpoint: /api/v1/stats, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stats"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["points"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("seasons="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("player_ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start_date="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end_date="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("game_ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("post_season="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start_time="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/stats"
)
req_collection.add_request(request)

# Endpoint: /api/v1/season_averages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("season_averages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1", examples=["20"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1", examples=["2"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("season="),
    primitives.restler_fuzzable_int("1", examples=["2019"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("player_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["123"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids[]="),
    primitives.restler_fuzzable_int("1", examples=["456"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("start_date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2020-01-01"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("end_date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["2020-12-31"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["points"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["desc"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("post_season="),
    primitives.restler_fuzzable_bool("true", examples=["true"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_ids="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/season_averages"
)
req_collection.add_request(request)

# Endpoint: /api/v1/teams/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["points"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/teams/{id}"
)
req_collection.add_request(request)

# Endpoint: /api/v1/games/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("games"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["Stephen%20Curry"]),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False, examples=["points"]),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: www.balldontlie.io\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/v1/games/{id}"
)
req_collection.add_request(request)
