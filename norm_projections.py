import pandas as pd


def calc_plus(points: pd.Series, num_starters: int) -> pd.Series:
    """ Series must be sorted in descending order by points"""
    starters_mean = points.iloc[:num_starters].mean()
    return points.divide(starters_mean)


def calc_weekly(points: pd.Series, weeks=16) -> pd.Series:
    return points.divide(weeks)

