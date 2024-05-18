import json
import glob
import click

jsons = glob.glob("data/jura*.json")
outputfile = "data/all_sets.json"

sets = []

skipped = []
counted = []

for j in jsons:
    # print(j)
    tournament = json.load(open(j))["tournament"]
    tournament_name = tournament["name"]
    tournament_slug = tournament["slug"]
    for event in tournament["events"]:
        event_name = event["name"]

        if event_name == "WAITING LIST" or "SF6" in event_name:
            skipped.append(f"{tournament_name} {event_name}")
            continue

        counted.append(f"{tournament_name} {event_name}")

        event_sets = event["sets"]["nodes"]

        for event_set in event_sets:
            event_set["slug"] = tournament_slug

        valid_event_sets = [s for s in event_sets if s["winnerId"] is not None]
        invalid_event_sets = [s for s in event_sets if s["winnerId"] is None]

        # if click.confirm(f"Keep '{tournament_name}'/'{event_name}' {len(event_sets)} ?"):
        sets.extend(valid_event_sets)

sets.sort(key=lambda l: l["id"])

print("skipped")
print("\n".join(skipped))

print("counted")
print("\n".join(counted))

json.dump(sets, open(outputfile, "w"))
