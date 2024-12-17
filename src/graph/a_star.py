import math
from collections import defaultdict
from typing import Literal

from src.graph.nodes import DictNodes
from src.graph.types import Key
from src.graph.utils import distance_nodes
from src.graph.ways import GraphWays



def a_star(
    graph_ways: GraphWays,
    dict_nodes: DictNodes,
    transport: Literal['car', 'bike', 'walk'],
    src: Key,
    dst: Key
  ) -> list[Key]:
  '''
  Implementation of A* algorithms
  Thanks to

  https://en.wikipedia.org/wiki/A*_search_algorithm
  https://gamedev.stackexchange.com/questions/49952/a-for-non-grid-network
  '''
  tr_idx = ['car', 'bike', 'walk'].index(transport)

  closed_set: set[Key] = set()
  open_set: set[Key] = {src}
  came_from = dict()

  g_score: dict[Key, float] = defaultdict(lambda: math.inf)
  f_score: dict[Key, float] = defaultdict(lambda: math.inf)
  g_score[src] = 0
  f_score[src] = _heuristic(graph_ways, src, dst)

  while open_set:
    current = min(open_set, key=f_score.__getitem__)

    if current == dst:
      return _reconstruct_path(came_from, current)

    open_set.remove(current)
    closed_set.add(current)

    adjacents = [item for item in graph_ways._data[current][1]]
    for key, spd, dist in adjacents:

      if key in closed_set:
        continue

      tentative_g_score = g_score[current] + dist * (130 - spd[tr_idx])

      if key not in open_set or tentative_g_score < g_score[key]:
        came_from[key] = current
        g_score[key] = tentative_g_score
        f_score[key] = tentative_g_score + _heuristic(graph_ways, key, dst)

        if key not in open_set:
          open_set.add(key)

  return []


def _heuristic(graph_ways: GraphWays, src: Key, dst: Key) -> float:
  src_pos = graph_ways._data[src][0]
  dst_pos = graph_ways._data[dst][0]
  return distance_nodes(*src_pos, *dst_pos)


def _reconstruct_path(came_from: dict[Key, Key], current: Key) -> list[Key]:
  total_path = [current]
  while current in came_from:
    current = came_from[current]
    total_path.insert(0, current)
  return total_path

