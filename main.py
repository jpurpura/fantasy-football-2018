import adj_projections as adj
import common as c

import sys
import numpy as np


def get_league_name():
    return sys.argv[1]


if __name__ == "__main__":
    # league_name = get_league_name()
    # adj.read_json(get_league_name(), SCORING_FILE)
    df = adj.get_projections("projections/espn_projections_aug_src.xlsx")
    league = get_league_name()
    scoring_dict = adj.read_json(league, c.SCORING)
    score_keys, score_vals = adj.separate_kv(scoring_dict)
    # print(df["QB"])
    # print(np.array(score_vals))
    # print(type(df["QB"][score_keys].loc[0].values))
    # print(df["QB"][score_keys].loc[0].dot(np.array(score_vals)))
    df_qb = adj.adj_scoring(df["QB"], score_keys, np.array(score_vals))
    df_qb = adj.separate_names_teams_pos(df_qb)
    print(df_qb)
