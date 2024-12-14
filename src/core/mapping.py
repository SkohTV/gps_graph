from math import sqrt
from dataclasses import dataclass

from src.api import load_cache


# http://theory.stanford.edu/~amitp/GameProgramming/MapRepresentations.html


@dataclass
class Node:
  x: float
  y: float


def _raw_distance_nodes_same_road(src: Node, dst: Node):
  return abs(sqrt(src.x**2 + src.y**2) - sqrt(dst.x**2 + dst.y**2))


def testing_loadall_nodes():
  tmp = []
  a, _, _ = load_cache()
  for i in a:
    if 'lat' in i and 'lon' in i:
      tmp.append(Node(x=i['lat'], y=i['lon']))

  print(_raw_distance_nodes_same_road(tmp[0], tmp[1]))
