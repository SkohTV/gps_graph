from typing import Any
import requests
from dataclasses import dataclass
from urllib.parse import quote



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

  print('Querying overpass-api...')

  # Build & send request
  data = "data=" + quote(data)
  r = requests.get(f'https://overpass-api.de/api/interpreter', data=data)

  # None return when error with API
  if (r.status_code != 200):
    raise requests.HTTPError()

  # Else build and return JSON_T wrapper around Any
  print('Request sucessfull')
  return OverpassResponse(r.json())
