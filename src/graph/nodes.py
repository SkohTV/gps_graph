import json
import statistics
from difflib import get_close_matches
from typing import Any

from src.graph.utils import distance_nodes, normalize_string, parse_tags
from src.consts import CACHE_FILE_COMPUTED_NODES_DATA, CACHE_FILE_COMPUTED_NODES_REL
from src.graph.ways import GraphWays
from src.logging import logger
from src.graph.types import ClosestNode, Item, Key, NodeWay, Position, Tags, Time
from src.utils import keys_to_int



class DictNodes:
  '''Represent all possible addresses'''

  def __init__(self, graph_ways: GraphWays) -> None:
    self._data: dict[Key, Item] = dict()
    self._relations: dict[Key, tuple[str, list[Key]]] = dict()
    self._graph_ways: GraphWays = graph_ways

    self.t = 0
    self.f = 0


  def load(self, data: list) -> None:
    '''Load a list of nodes into the dict'''

    logger.debug('Loading all nodes into DictNodes')

    relations = []
    nodes = []
    ways = []

    for d in data:
      match d['type']:
        case 'node':
          nodes.append(d)
        case 'way':
          ways.append(d)
        case 'relation':
          relations.append(d)

    # We use relations to put nodes in self._data and find their closest NodeWay
    for idx, r in enumerate(relations):
      logger.debug(f'Loading relation[{idx+1}/{len(relations)}]')
      self.handle_relation(r)

    for idx, n in enumerate(nodes):
      logger.debug(f'Loading node[{idx+1}/{len(nodes)}]')
      self.handle_node(n)

    for idx, w in enumerate(ways):
      logger.debug(f'Loading way[{idx+1}/{len(ways)}]')
      self.handle_way(w)

    logger.info(f'Loaded all nodes: found=({self.t});not_found=({self.f});precision=({self.t/(self.t+self.f)*100:2f}%)')


  def handle_relation(self, relation: dict) -> None:
    '''Parse an item of type relation'''
    ways: list[Key] = []
    nodes: list[Key] = []
    nodes_pos: list[Position] = []
    tags: Tags = parse_tags(relation['tags'])

    for r in relation['members']:

      if r['type'] == 'way':
        if r['ref'] not in self._graph_ways._ways:
          self.f += 1
          return # If we don't have this way stored, then it's not a road, so we cancel this relation
        ways.append(r['ref'])

      elif r['type'] == 'node':
        nodes.append(r['ref'])
        nodes_pos.append((r['lat'], r['lon']))
      # We ignore relations in relations, to hard to bother with it

    if not ways:
      self.f += 1
      return # If there is no way in relation, then we ignore (stuff like 'Place du General Leclerc')

    closest = [self.find_closest_node(np, ways) for np in nodes_pos]

    for key, pos, clos in zip(nodes, nodes_pos, closest):
      self.generate_node(key, pos, clos, tags) # We use tags of the associatedStreet for street name

    self._relations[relation['id']] = (relation['tags']['name'], ways)
    self.t += 1


  def handle_node(self, node: dict) -> None:
    '''Parse an item of type node'''
    key: Key = node['id'] 

    position: Position = (node['lat'], node['lon'])
    tags: Tags = parse_tags(node['tags'])

    possible_streets = self.find_street_name(node)

    if possible_streets is None:
      self.f += 1
      return

    # Build item
    closest = self.find_closest_node(position, possible_streets)
    item: Item = (position, closest, tags)

    self._data[key] = item
    self.t += 1

  
  def handle_way(self, way: dict) -> None:
    '''Parse an item of type way'''
    key = way['id']
    geo = way['geometry']

    # Position is average of all nodes that makes the way
    position: Position = (statistics.mean([x['lat'] for x in geo]), statistics.mean([x['lon'] for x in geo]))

    tags: Tags = parse_tags(way['tags'])
    street_name_possible = self.find_street_name(way)

    if street_name_possible is None:
      self.f += 1
      return

    closest = self.find_closest_node(position, street_name_possible)

    item: Item = (position, closest, tags)

    self._data[key] = item
    self.t += 1
    

  ## UTILITY FUNCTIONS

  def generate_node(self, key: Key, position: Position, closest: ClosestNode, tags: Tags) -> None:
    '''Generate a node from data'''
    self._data[key] = (position, closest, tags)


  def find_closest_node(self, pos: Position, ways: list[Key]) -> Key:
    '''Find the closest NodeWay to a node, given a list of possible ways'''
    all_ways: list[list[Key]] = [self._graph_ways._ways[idx] for idx in ways]
    all_nodes: dict[Key, NodeWay] = {n: self._graph_ways._data[n] for ns in all_ways for n in ns}
    min_dist: dict[Key, float] = {key: distance_nodes(*pos, *val[0]) for key, val in all_nodes.items()}
    index_min: Key = min(min_dist, key=min_dist.get) # type: ignore
    return index_min

  
  def find_street_name(self, data: dict[str, Any]) -> list[Key]|None:
    '''
    Find the street name from a way or a node
    We need to normalize BECAUSE THERE ARE TYPOS WTF ??
    '''
    # First, find the street name
    possible_streets = []
    street_name = ''

    if 'addr:street' in data['tags']:
      street_name = normalize_string(data['tags']['addr:street'])

    elif 'contact:street' in data['tags']:
      street_name = normalize_string(data['tags']['contact:street'])

    else:
      self.f += 1
      return # If the node has no link to any street, then we ignore the node


    # Then compare to existing street names
    if street_name in self._graph_ways._named_ways:
      possible_streets = self._graph_ways._named_ways[street_name]

    elif (norm := get_close_matches(street_name, self._graph_ways._named_ways.keys(), n=1)):
      possible_streets = self._graph_ways._named_ways[norm[0]]

    else:
      return None # Only 50 have weird name like "R N 13", we ignore them, I hate them

    # And return ofc
    return possible_streets



  def save_to_file(self) -> None:
    '''Save the big data to files to avoid recompute'''
    logger.info('Saving nodes_data to file')
    with open(CACHE_FILE_COMPUTED_NODES_DATA, 'w') as f:
      json.dump(self._data, f)

    logger.info('Saving nodes_relations to file')
    with open(CACHE_FILE_COMPUTED_NODES_REL, 'w') as f:
      json.dump(self._relations, f)


  def load_from_file(self) -> None:
    '''Load the big data from the cached json'''
    logger.info('Loading nodes_data from file')
    with open(CACHE_FILE_COMPUTED_NODES_DATA) as f:
      self._data = json.load(f, object_pairs_hook=keys_to_int) # type: ignore

    logger.info('Loading nodes_relations from file')
    with open(CACHE_FILE_COMPUTED_NODES_REL) as f:
      self._relations = json.load(f, object_pairs_hook=keys_to_int) # type: ignore

