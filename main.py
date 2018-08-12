import adj_projections as adj
import norm_projections as nrm
import util
import constants as c

import numpy as np
import pandas as pd

import datetime

def main():
    league = util.get_league_name()
    prj = adj.get_projections(c.PROJECTIONS_PATH)
    scoring_dict = util.read_json(league, c.SCORING)
    roster_dict = util.read_json(league, c.ROSTER)
    score_keys, score_vals = util.separate_kv(scoring_dict)
    pos_dataframe_dict = {}

    flex_points = []
    flex_starters = 10 + sum(roster_dict[f] * roster_dict[c.LEAGUE_SIZE]
                             for f in c.FLEX_POSITIONS)

    for position, pos_df in prj.items():
        pos_df = pos_df.drop(c.POINTS, axis=1)

        # Clean up player names
        names, teams, pos = adj.separate_names_teams_pos(pos_df[c.PLAYER])
        pos_df[c.PLAYER] = names
        pos_df.insert(2, c.TEAM, teams)
        pos_df.insert(3, c.POS, pos)

        # Calculate league points and remove original points
        new_pts = adj.adj_scoring(pos_df[score_keys], np.array(score_vals))
        pos_df.insert(4, c.POINTS, new_pts)
        pos_df[c.RANK] = pos_df[c.POINTS].rank(method="max", ascending=False)
        pos_df = pos_df.set_index(c.RANK)
        pos_df.insert(4, "PPG", nrm.calc_weekly(new_pts))
        pos_df = adj.sort_by_pts(pos_df)

        # Add plus and norm stats
        pos_starters = roster_dict[position] * roster_dict[c.LEAGUE_SIZE]
        pos_plus = nrm.calc_plus(pos_df[c.POINTS], pos_starters)
        pos_df.insert(5, "POS+", pos_plus)

        if position in c.FLEX_POSITIONS:
            top_values = pos_df[c.POINTS].iloc[:flex_starters].values.tolist()
            flex_points.extend(top_values)
        pos_df = pos_df.round(3)
        pos_dataframe_dict[position] = pos_df

    flex_points.sort(reverse=True)
    flex_points = flex_points[:flex_starters]

    for pos in c.FLEX_POSITIONS:
        pos_df = pos_dataframe_dict[pos]
        flex_plus = pos_df[c.POINTS].divide(pd.Series(flex_points).mean())
        pos_df.insert(6, "FLEX+", flex_plus.round(3))

    print(pos_df)
    today_date = datetime.datetime.today().strftime('%Y-%m-%d')
    excel_file = "{}/updated_projections{}.xlsx".format(league, today_date)
    writer = pd.ExcelWriter(excel_file, engine="xlsxwriter")
    workbook = writer.book
    for pos, pos_df in pos_dataframe_dict.items():
        worksheet = workbook.add_worksheet(pos)
        writer.sheets[pos] = worksheet
        pos_df.to_excel(writer, sheet_name=pos)


if __name__ == "__main__":
    main()
