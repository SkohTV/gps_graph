import json

from src.logging import logger
from src.graph.types import EdgeWay, Key, NodeWay, Position
from src.graph.utils import get_speed, distance_direction_nodes



class GraphWays:
  '''Represent a graph of roads'''

  def __init__(self) -> None:
    self._data: dict[Key, NodeWay] = dict()
    self._ways: dict[Key, list[Key]] = dict()


  def load(self, data: list) -> None:
    '''Load a list of ways into the graph'''

    logger.debug('Loading all ways into GraphWays')

    # Loop over all data
    for d in data:

      # We ignore nodes and relations
      if d['type'] != 'way':
        continue

      d_geometry = d['geometry']
      d_nodes = d['nodes']
      d_speed = get_speed(d['tags']['highway'])
      self._ways[d['id']] = d_nodes

      ord_nodes: list[NodeWay] = []
      ord_edges: list[EdgeWay] = []
      rev_edges: list[EdgeWay] = []

      for g in d_geometry:
        pos: Position = (g['lat'], g['lon'])
        node: NodeWay = (pos, list())
        ord_nodes.append(node)

      it = zip(ord_nodes, d_nodes)
      n1, idx1 = it.__next__()
      for n2, idx2 in it:
        dist, dir = distance_direction_nodes(n1[0][0], n1[0][1], n2[0][0], n2[0][1])
        ord_edges.append((idx2, d_speed, dist, dir))
        rev_edges.append((idx1, d_speed, dist, ((dir + 180) % 360)))

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

