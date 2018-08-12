import common as c

import pandas as pd
import numpy as np
import json

def read_json(league: str, league_file: str) -> dict:
    with open("{}/{}.json".format(league, league_file)) as f:
        data = json.load(f)
    return data


def get_projections(projections_file: str):
    return pd.read_excel(projections_file, sheet_name=None)


def adj_scoring(df: pd.DataFrame, score_keys: list, score_vals: np.array):
    df[c.POINTS] = df[score_keys].apply(lambda r: r.dot(score_vals), axis=1)
    return df


def separate_kv(d: dict) -> ([str], [str]):
    keys = list(d)
    values = [d[key] for key in keys]
    return keys, values


def separate_names_teams_pos(df: pd.DataFrame) -> pd.DataFrame:
    player_names = df[c.PLAYER].values
    names = []
    teams = []
    positions = []
    for value in player_names:
        name, other = value.strip().split(",", maxsplit=1)
        team, position = other.strip().split(" ", maxsplit=1)
        names.append(name)
        teams.append(team)
        positions.append(position)
    df[c.PLAYER] = names
    df.insert(2, c.TEAM, teams)
    df.insert(3, c.POS, positions)
    return df
