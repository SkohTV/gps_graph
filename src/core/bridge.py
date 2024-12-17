from __future__ import annotations

from src.api_icloud import Icloud
from src.core.tags import TagsDict
from src.graph.nodes import DictNodes
from src.graph.ways import GraphWays
from src.graph.types import Position






# Yes pyright, I know it's a NoneType, but let's pretend it's a BridgeApi ok ?
bridgge_api: BridgeApi
bridge_api = None # type: ignore


class BridgeApi:
  '''An API that bridge the gap between front and back end'''

  def __init__(self, g: GraphWays, d: DictNodes, t: TagsDict, i: Icloud) -> None:
    self.graph_ways = g
    self.dict_nodes = d
    self.tags_dict = t
    self.icloud = i


  def get_location(self) -> Position:
    return self.icloud.gps_request()

  
  def get_possible_addresse(self, string: str):
    possible_nodes = self.tags_dict.search_for_tags(string)
    # print([self.dict_nodes._data[x] for x in possible_nodes])


  def get_path_to_dest(self, src: Position, dst: Position):
    ...


