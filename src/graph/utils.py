import math
from typing import Any
from unidecode import unidecode

from src.graph.types import MaxSpeed


def distance_nodes(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
  '''
  Compute the distance between 2 points on a sphere

  https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
  https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
  https://en.wikipedia.org/wiki/Haversine_formula

  https://www.movable-type.co.uk/scripts/latlong.html
  '''
  lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
  dlon = lon2 - lon1 
  dlat = lat2 - lat1 
  a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
  c = 2 * math.asin(math.sqrt(a)) 
  r = 6371 # Radius of earth in kilometers. 
  dist = c * r

  # We don't need direction :,(
  # y = math.sin(lon2 - lon1) * math.cos(lat2)
  # x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
  # th = math.atan2(y, x)
  # dir = (th * 180 / math.pi + 360) % 360;
  
  return round(dist, 4)#, round(dir, 4)


def normalize_string(val: str) -> str:
  '''Remove accents, spaces and lower the string'''
  return unidecode(val.lower().replace(' ', '-'))


VALID_TAGS = [
  normalize_string('addr:city'),
  normalize_string('addr:housenumber'),
  normalize_string('addr:postcode'),
  normalize_string('addr:street'),
  normalize_string('name'),
  normalize_string('brand'),
  normalize_string('contact:street'),
  normalize_string('shop'),
]

# I'm not gonna bother fighting json.load(object_pairs_hook=) for typing
def parse_tags(tags: Any) -> list[str]:
  '''Parse a list of tags and select only some of them'''
  # print([normalize_string(val) for key, val in tags.items() if key in VALID_TAGS])
  return [normalize_string(val) for key, val in tags.items() if key in VALID_TAGS]

