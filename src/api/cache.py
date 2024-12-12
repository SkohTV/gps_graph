import json
import os

from src.api.requests import QUERY_NODES, QUERY_WAYS, query_overpass_api

CACHE_DIR = os.path.join(os.getcwd(), '.cache')


def update_cache_map(force = False):
  '''
  Update the json files containing all nodes and way fetched
  Be careful, these updates can take a few minutes
  '''

  # If there is already a FILE named .cache (wtf is wrong with you...)
  if os.path.isfile(CACHE_DIR):
    raise FileExistsError

  # Create directory
  if not os.path.isdir(CACHE_DIR):
    os.makedirs(CACHE_DIR)

  # Remove the cache and update it
  if not os.scandir(CACHE_DIR) or force:

    # Cache nodes
    with open(os.path.join(CACHE_DIR, 'nodes.json'), 'w') as f:
      nodes = query_overpass_api(QUERY_NODES)
      json.dump(nodes.items(), f)
     
    # Cache ways
    with open(os.path.join(CACHE_DIR, 'ways.json'), 'w') as f:
      ways = query_overpass_api(QUERY_WAYS)
      json.dump(ways.items(), f)


# create function to fix file not existant or erroneous

def load_cache(force = False):
  ...

  


