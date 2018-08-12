import adj_projections as adj
import norm_projections as nrm
import util
import constants as c

import numpy as np


def main():
    league = util.get_league_name()
    prj = adj.get_projections(c.PROJECTIONS_PATH)
    scoring_dict = util.read_json(league, c.SCORING)
    roster_dict = util.read_json(league, c.ROSTER)
    score_keys, score_vals = util.separate_kv(scoring_dict)
    pos_dataframe_dict = {}

    for position, pos_df in prj.items():
        # Clean up player names
        names, teams, pos = adj.separate_names_teams_pos(pos_df)
        pos_df[c.PLAYER] = names
        pos_df.insert(2, c.TEAM, teams)
        pos_df.insert(3, c.POS, pos)

        # Calculate league points and remove original points
        new_pts = adj.adj_scoring(pos_df[score_keys], np.array(score_vals))
        pos_df.insert(4, c.POINTS, new_pts)

        pos_df = adj.sort_by_pts(pos_df)
        pos_dataframe_dict[position] = pos_df

    for pos, pos_df in pos_dataframe_dict.items():
        print(pos)
        print(pos_df)


if __name__ == "__main__":
    main()
