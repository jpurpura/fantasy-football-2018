import pandas as pd


def calc_plus(points: pd.Series, num_players: int) -> pd.Series:
    """ Series must be sorted in descending order by points"""
    starters_mean = points.iloc[:num_players].mean()
    return points.divide(starters_mean)


def calc_weekly(points: pd.Series, weeks=16) -> pd.Series:
    return points.divide(weeks)


def calc_zscore_norm(points: pd.Series, num_players: int) -> pd.Series:
    mean_diff = points - points.mean()
    return mean_diff.divide(points.std())
