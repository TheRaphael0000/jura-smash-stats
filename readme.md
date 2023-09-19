# jura-smash-stats

a simple set of scripts to create a PowerRanking for my weekly in Jura.

i download the sets on start.gg and apply the elo rating algorithm on the set results

## workflow

0. set the tournaments slug in `tournaments.json`
1. call `python import_startgg.py` to download the tournaments
2. call `python merge_events.py` to centerlize all the sets to analyses in a single file
3. use `jura_stats.ipynb` to work on the stats

## todo

this needs to be discussed with the admins:

- exclude players with few sets from the computation
- find a good k which correctly reflect the level of the participants