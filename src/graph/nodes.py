import json
import sys
from typing import TypeAlias

from src.graph.utils import distance_direction_nodes
from src.consts import VALID_TAGS
from src.graph.ways import GraphWays
from src.logging import logger
from src.graph.types import ClosestNode, Item, Key, NodeWay, Position, Tags







class DictNodes:
  '''Represent all possible addresses'''

  def __init__(self, graph_ways: GraphWays) -> None:
    self._data: dict[Key, Item] = dict()
    self._relations: dict[Key, tuple[str, list[Key]]] = dict()
    self._graph_ways: GraphWays = graph_ways


  def load(self, data: list) -> None:
    '''Load a list of nodes into the dict'''

    logger.debug('Loading all nodes into DictNodes')

    relations = []
    nodes = []
    ways = []

    a = {}
    for d in data:
      if d['type'] in a:
        a[d['type']].append(d)
      else:
        a[d['type']] = [d]

      match d['type']:
        case 'node':
          nodes.append(d)
        case 'way':
          ways.append(d)
        case 'relation':
          relations.append(d)

    # We use relations to put nodes in self._data and find their closest NodeWay
    for r in relations:
      self.handle_relation(r)

    for n in nodes:
      self.handle_node(n)

    # print(json.dumps(a['node'][99]))
    # print(json.dumps(a['relation'][99]))
    # print(json.dumps(a['way'][99]))


  # def find_closest_node(self, ways: list[Key], node: Key) -> Key:
  #   # real_ways = [self._graph_ways._data[w] for way in ways]
  #
  #
  #   for n in
  #   dist, _ = distance_direction_nodes()
    


  def handle_relation(self, relation: dict) -> None:
    '''Parse an item of type relation'''
    ways: list[Key] = []
    nodes: list[Key] = []
    nodes_pos: list[Position] = []

    for r in relation['members']:

      if r['type'] == 'way':
        if r['ref'] not in self._graph_ways._ways:
          return # If we don't have this way stored, then it's not a road, so we cancel this relation
        ways.append(r['ref'])

      elif r['type'] == 'node':
        nodes.append(r['ref'])
        nodes_pos.append((r['lat'], r['lon']))
      # We ignore relations in relations, to hard to bother with it

    if not ways:
      return # If there is no way in relation, then we ignore (stuff like 'Place du General Leclerc')

    closest = [self.find_closest_node(np, ways) for np in nodes_pos]

    for key, pos, clos in zip(nodes, nodes_pos, closest):
      self.generate_node(key, pos, clos, Tags()) # We have no tags yet

    self._relations[relation['id']] = (relation['tags']['name'], ways)



  def generate_node(self, key: Key, position: Position, closest: ClosestNode, tags: Tags) -> None:
    '''Generate a node from data'''
    self._data[int(key)] = (position, closest, tags)


  def handle_node(self, node: dict) -> None:
    '''Parse an item of type node'''
    key: Key = node['id'] 

    position: Position = (node['lat'], node['lon'])
    tags: Tags = self.parse_tags(node['tags'])

    # print(node)


    # if street_name not in self._streets:
    #   return # If we have no relation with street_name, give up

    # closest = self.find_closest_node(position, self._streets[street_name])
    #
    # item: Item = (position, closest, tags)
    #
    # self._data[key] = item
    # print(key, item)



  def parse_tags(self, tags: dict[str, str]) -> dict[str, str]:
    '''Parse a list of tags and select only some of them'''
    return {key: val for key, val in tags.items() if key in VALID_TAGS}


  def find_closest_node(self, pos: Position, ways: list[Key]) -> Key:
    '''Find the closest NodeWay to a node, given a list of possible ways'''
    all_ways: list[list[Key]] = [self._graph_ways._ways[idx] for idx in ways]
    all_nodes: dict[Key, NodeWay] = {n: self._graph_ways._data[n] for ns in all_ways for n in ns}
    min_dist: dict[Key, float] = {key: distance_direction_nodes(*pos, *val[0])[0] for key, val in all_nodes.items()}
    index_min: Key = min(min_dist, key=min_dist.get) # type: ignore
    return index_min

