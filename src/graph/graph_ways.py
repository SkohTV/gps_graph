import json
import math
from typing import TypeAlias


# MODULARITY

Key: TypeAlias = int

Position: TypeAlias = tuple[float, float]
MaxSpeed: TypeAlias = int
Distance: TypeAlias = float
Direction: TypeAlias = float

Edge: TypeAlias = tuple[Key, MaxSpeed, Distance, Direction]
Node: TypeAlias = tuple[Position, list[Edge]]


def get_speed(highway: str) -> int:
  '''Convert the highway type into the speed limit of this type of road'''
  match highway:
    case 'residential':
      return 50
    case _:
      return 90


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
  r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
  dist = c * r

  y = math.sin(lon2 - lon1) * math.cos(lat2)
  x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
  th = math.atan2(y, x)
  dir = (th * 180 / math.pi + 360) % 360;
  
  return round(dist, 4), round(dir, 4)



class GraphWays:
  '''Represent a graph of roads'''

  def __init__(self) -> None:
    self._data: dict[Key, Node] = dict()


  def load(self, data: list) -> None:
    '''Load a list of ways into the graph'''

    for d in data:

      # We ignore nodes and relations
      if d['type'] != 'way':
        continue

      d_geometry = d['geometry']
      d_nodes = d['nodes']
      # max_speed = get_speed(d['tags']['highway'])

      ord_nodes: list[Node] = []
      ord_edges: list[Edge] = []
      rev_edges: list[Edge] = []

      for g in d_geometry:
        pos: Position = (g['lat'], g['lon'])
        node: Node = (pos, list())
        ord_nodes.append(node)

      it = zip(ord_nodes, d_nodes)
      n1, idx1 = it.__next__()
      for n2, idx2 in it:
        dist, dir = distance_direction_nodes(n1[0][0], n1[0][1], n2[0][0], n2[0][1])
        spd = get_speed('TEMP')
        ord_edges.append((idx2, spd, dist, dir))
        rev_edges.append((idx1, spd, dist, ((dir + 180) % 360)))

      for idx, itm in enumerate(ord_edges):
        ord_nodes[idx][1].append(itm)

      l = len(ord_nodes) - 1
      for idx, itm in enumerate(reversed(rev_edges)):
        ord_nodes[l - idx][1].append(itm)

      for idx, node in zip(d_nodes, ord_nodes):

        if idx in self._data:
          self._data[idx][1].extend(node[1])
        else:
          self._data[idx] = node

