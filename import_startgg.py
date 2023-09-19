import asyncio
import json
import os
from pprint import pprint
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

config = json.load(open("config.json"))

headers = {
    "Authorization": f"Bearer {config['start_gg_api_key']}"
}

options = {"url": "https://api.start.gg/gql/alpha", "headers": headers}

transport = AIOHTTPTransport(**options)
client = Client(transport=transport, fetch_schema_from_transport=True)

tournaments = json.load(open("tournaments.json"))

for slug in tournaments:
    print(slug)
    filename = f"data/{slug}.json"

    if os.path.exists(filename):
        print("cache")
        continue

    query = gql(
        """
query func {
tournament(slug: \"""" + slug + """\") {
  name
  slug
  events {
    name
    sets(page: 0, perPage: 400) {
      nodes {
        id
        winnerId
        slots {
          entrant {
            id
            name
            participants {
            player {
              id
            }
            }
          }
        }
      }
    }
  }
}
}
  """
    )

    events = client.execute(query)
    json.dump(events, open(filename, "w"))
    print("saved")
