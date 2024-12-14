import os
import json
import requests as req
from typing import Any
from urllib.parse import quote
from dataclasses import dataclass

from src.api.requests import QUERY_NODES, QUERY_WAYS_ALL, QUERY_WAYS_ALL
from src.logging import logger
from src.consts import CACHE_DIR, CACHE_FILE_NODES, CACHE_FILE_WAYS_ALL, CACHE_FILE_WAYS_CAR



# json returned by requests are Any, but this avoid confusing JSON_T with Any
@dataclass
class OverpassResponse:
  '''Wrapper around an overpass response'''
  _data: dict[str, Any]
  
  def items(self) -> list:
    return self._data['elements']



def query_overpass_api(data: str) -> OverpassResponse:
  '''Send a request to overpass-api with unquoted {data}'''

  logger.info('Querying overpass-api...')

  # Build & send request
  data = "data=" + quote(data)
  r = req.get(f'https://overpass-api.de/api/interpreter', data=data)

  # None return when error with API
  if (r.status_code != 200):
    raise req.HTTPError()

  # Else build and return JSON_T wrapper around Any
  logger.info('Request sucessfull')
  return OverpassResponse(r.json())



def update_cache(force = False) -> None:
  '''
  Update the json files containing all nodes and way fetched
  Be careful, these updates can take a few minutes
  '''

  # Remove the cache and update it
  if not os.scandir(CACHE_DIR) or force:

    # Cache nodes
    with open(CACHE_FILE_NODES, 'w') as f:
      nodes = query_overpass_api(QUERY_NODES)
      json.dump(nodes.items(), f)
     
    # Cache car ways
    with open(CACHE_FILE_WAYS_CAR, 'w') as f:
      ways = query_overpass_api(QUERY_WAYS_ALL)
      json.dump(ways.items(), f)

    # Cache walk bike ways
    with open(CACHE_FILE_WAYS_ALL, 'w') as f:
      ways = query_overpass_api(QUERY_WAYS_ALL)
      json.dump(ways.items(), f)



def load_cache() -> tuple:
  '''Load the json cached files into objects'''

  # Load nodes
  logger.debug('Loading nodes into object')
  with open(CACHE_FILE_NODES) as f:
    nodes = json.load(f)

  # Load nodes
  logger.debug('Loading car ways into object')
  with open(CACHE_FILE_WAYS_CAR) as f:
    ways_car = json.load(f)

  # Load nodes
  logger.debug('Loading all ways into object')
  with open(CACHE_FILE_WAYS_ALL) as f:
    ways_all = json.load(f)

  logger.debug('All files loaded')

  return (nodes, ways_car, ways_all)

