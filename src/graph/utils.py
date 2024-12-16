import math
from src.graph.types import MaxSpeed



def get_speed(highway: str) -> MaxSpeed:
  '''
  Convert the highway type into the speed limit of this type of road
  https://wiki.openstreetmap.org/wiki/Key:highway
  '''

  match highway:
    case 'residential':
      return (50, 0, 0)
    case _:
      return (90, 0, 0)


def distance_direction_nodes(lat1: float, lon1: float, lat2: float, lon2: float) -> tuple[float, float]:
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

  y = math.sin(lon2 - lon1) * math.cos(lat2)
  x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
  th = math.atan2(y, x)
  dir = (th * 180 / math.pi + 360) % 360;
  
  return round(dist, 4), round(dir, 4)

