# fantasy-football-2018
[ESPN Fantasy Football Projections](http://games.espn.com/ffl/tools/projections?&startIndex=40), adjusted for league scoring

## Usage
1. Create a directory with the league name, e.g. "fries".
2. Add a scoring.json to the league's directory for the league's scoring settings, example shown in fries/scoring.json
3. Add a roster.json to the league's directory for the league's roster settings, example shown in fries/roster.json
3. Run script:
`python main.py league_name`

## Glossary
`FLEX` 
WR, RB, or TE

`POS+` 
The player's projected points compared to the projected points of the average starter at his position.  
*Example:*  
  WR John Smith has a `POS+` of 120. John Smith is projected for 20% more points than the average starting WR in the specified league.
 
 `FLEX+` 
The player's projected points compared to the projected points of the average starter of all FLEX positions.  
*Example:*  
RB John Doe has a `FLEX+` of 110. John Doe is projected for 10% more points than the average starting RB, WR, TE, and RB/WR/TE slots in the specified league.
  
`RB1+`, `RB2+`, etc.
The player's projected points compared to the projected points of the average starter at that slot.  
*Example:*  
  WR John Smith has a `WR1+` of 110 and a `WR2+` of 130. John Smith is projected for 10% more points than the average starting WR1 and 30% more points than the average starting WR2 in the specified league.
