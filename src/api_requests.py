from typing import Any
import requests
from dataclasses import dataclass
from urllib.parse import quote
import json
import os

from src.consts import CACHE_DIR
from src.logging import logger



# AREA_ID = '3600149197' # Caen
AREA_ID = '3600007453' # Calvados
TIMEOUT = 25

QUERY_NODES = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["amenity"](area.searchArea);
  nwr["addr:housenumber"](area.searchArea);
  out geom;
'''

QUERY_WAYS = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["highway"](area.searchArea);
  out geom;
'''



# json returned by requests are Any, but this avoid confusing JSON_T with Any
@dataclass
class OverpassResponse:
  '''Wrapper around an overpass response'''
  _data: dict[str, Any]
  
  def items(self) -> list:
    return self._data['elements']



def query_overpass_api(data: str) -> OverpassResponse:
  '''Send a request to overpass-api with unquoted {data}'''

  logger.debug('Querying overpass-api...')

  # Build & send request
  data = "data=" + quote(data)
  r = requests.get(f'https://overpass-api.de/api/interpreter', data=data)

  # None return when error with API
  if (r.status_code != 200):
    raise requests.HTTPError()

  # Else build and return JSON_T wrapper around Any
  logger.debug('Request sucessfull')
  return OverpassResponse(r.json())



def update_cache_map(force = False):
  '''
  Update the json files containing all nodes and way fetched
  Be careful, these updates can take a few minutes
  '''

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

