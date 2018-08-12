import sys
import json


def get_league_name():
    return sys.argv[1]


def read_json(league: str, league_file: str) -> dict:
    with open("{}/{}.json".format(league, league_file)) as f:
        data = json.load(f)
    return data
