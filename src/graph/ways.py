import json

from src.core.speed import get_speed
from src.consts import CACHE_FILE_COMPUTED_WAYS_DATA, CACHE_FILE_COMPUTED_WAYS_NAME, CACHE_FILE_COMPUTED_WAYS_WAYS
from src.logging import logger
from src.graph.types import EdgeWay, Key, NodeWay, Position
from src.graph.utils import distance_nodes, normalize_string
from src.utils import keys_to_int



class GraphWays:
  '''Represent a graph of roads'''

  def __init__(self) -> None:
    self._data: dict[Key, NodeWay] = dict()
    self._ways: dict[Key, list[Key]] = dict()
    self._named_ways: dict[str, list[Key]] = dict()


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

      if 'name' in d['tags']:
        street_name = normalize_string(d['tags']['name'])

        if street_name in self._named_ways:
          self._named_ways[street_name].append(d['id'])
        else:
          self._named_ways[street_name] = [d['id']]


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
        dist = distance_nodes(n1[0][0], n1[0][1], n2[0][0], n2[0][1])
        ord_edges.append((idx2, d_speed, dist))
        rev_edges.append((idx1, d_speed, dist))

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


  def save_to_file(self) -> None:
    '''Save the big data to files to avoid recompute'''
    logger.info('Saving ways_data to file')
    with open(CACHE_FILE_COMPUTED_WAYS_DATA, 'w') as f:
      json.dump(self._data, f)

    logger.info('Saving ways_ways to file')
    with open(CACHE_FILE_COMPUTED_WAYS_WAYS, 'w') as f:
      json.dump(self._ways, f)

    logger.info('Saving ways_named_ways to file')
    with open(CACHE_FILE_COMPUTED_WAYS_NAME, 'w') as f:
      json.dump(self._named_ways, f)


  def load_from_file(self) -> None:
    '''Load the big data from the cached json'''
    logger.info('Loading ways_data from file')
    with open(CACHE_FILE_COMPUTED_WAYS_DATA) as f:
      self._data = json.load(f, object_pairs_hook=keys_to_int) # type: ignore

    logger.info('Loading ways_ways from file')
    with open(CACHE_FILE_COMPUTED_WAYS_WAYS) as f:
      self._ways = json.load(f, object_pairs_hook=keys_to_int) # type: ignore

    logger.info('Loading ways_name from file')
    with open(CACHE_FILE_COMPUTED_WAYS_NAME) as f:
      self._named_ways = json.load(f)

