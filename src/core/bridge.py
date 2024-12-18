from __future__ import annotations
from typing import Literal, get_args

from src.graph.a_star import a_star
from src.api_icloud import Icloud
from src.core.tags import TagsDict
from src.graph.nodes import DictNodes
from src.graph.ways import GraphWays
from src.graph.types import Key, Position



class BridgeApi:
  '''An API that bridge the gap between front and back end'''

  def __init__(self, g: GraphWays, d: DictNodes, t: TagsDict, i: Icloud) -> None:
    self.graph_ways = g
    self.dict_nodes = d
    self.tags_dict = t
    self.icloud = i


  def get_location(self) -> Position:
    '''Return the user phone location'''
    return self.icloud.gps_request()

  def get_possible_addresse(self, string: str) -> list[tuple[Position, str, Key]]:
    '''Take a user string and check which address is most likely to be searched'''
    possible_nodes = self.tags_dict.search_for_tags(string)
    nodes = [self.dict_nodes._data[x] for x in possible_nodes]
    return [(pos, self._beautify_tags(tags), close) for pos, close, tags in nodes]


  def get_path_to_dest(self, src: Position, dst: Key, transport: str):
    '''Bridge between UI and A*'''
    frm = self.graph_ways.slow_find_closest_node(src)
    to = dst

    # Getting rid of typing errors :)
    assert transport in get_args(Literal['car', 'bike', 'walk'])

    key_list = a_star(self.graph_ways, self.dict_nodes, transport, frm, to)
    return [self.graph_ways._data[k][0] for k in key_list]


  def _beautify_tags(self, tags: list[str]) -> str:
    '''Give a new youth to the tags'''
    return ', '.join(tags).title().replace('-', ' ')

