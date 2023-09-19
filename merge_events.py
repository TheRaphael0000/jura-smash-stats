import json
import glob
import click

jsons = glob.glob("data/jura*.json")
outputfile = "data/all_sets.json"

sets = []

for j in jsons:
    print(j)
    tournament = json.load(open(j))["tournament"]
    for event in tournament["events"]:
        event_name = event["name"]
        event_sets = event["sets"]["nodes"]

        valid_event_sets = [s for s in event_sets if s["winnerId"] is not None]
        invalid_event_sets = [s for s in event_sets if s["winnerId"] is None]

        print(event_name, invalid_event_sets)

        # if click.confirm(f"Keep '{tournament_name}'/'{event_name}' {len(event_sets)} ?"):
        sets.extend(valid_event_sets)

sets.sort(key=lambda l: l["id"])

json.dump(sets, open(outputfile, "w"))
