import constants as c

import pandas as pd
import numpy as np
import json



def get_projections(projections_file: str):
    return pd.read_excel(projections_file, sheet_name=None)


def adj_scoring(df: pd.DataFrame, score_keys: list, score_vals: np.array):
    df[c.POINTS] = df[score_keys].apply(lambda r: r.dot(score_vals), axis=1)
    return df


def separate_names_teams_pos(player_names: np.array) -> ([str], [str], [str]):
    names = []
    teams = []
    positions = []
    for value in player_names:
        name, other = value.strip().split(",", maxsplit=1)
        team, position = other.strip().split(" ", maxsplit=1)
        names.append(name)
        teams.append(team)
        positions.append(position)
    # names_series[c.PLAYER] = names
    # names_series.insert(2, c.TEAM, teams)
    # names_series.insert(3, c.POS, positions)
    return names, teams, positions


def sort_by_pts(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(c.POINTS, ascending=False)
