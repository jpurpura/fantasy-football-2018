import adj_projections as adj
import common as c

import sys
import numpy as np


def get_league_name():
    return sys.argv[1]


def main():
    league = get_league_name()
    prj = adj.get_projections(c.PROJECTIONS_PATH)
    scoring_dict = adj.read_json(league, c.SCORING)
    score_keys, score_vals = adj.separate_kv(scoring_dict)
    adj_prj = {}
    for position, pos_df in prj.items():
        pos_df = adj.adj_scoring(pos_df, score_keys, np.array(score_vals))
        pos_df = adj.separate_names_teams_pos(pos_df)
        pos_df = adj.sort_by_pts(pos_df)
        adj_prj[position] = pos_df
    for pos, pos_df in adj_prj.items():
        print(pos)
        print(pos_df)



if __name__ == "__main__":
    main()
