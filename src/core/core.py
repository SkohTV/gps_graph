from __future__ import annotations
from dataclasses import dataclass

from api.api import query_all_nodes_caen


@dataclass
class Tag:
  name: str
  list: Item


@dataclass
class Item:
  name: str
  list: Tag


# Check quad tree
def build_items_tags() -> tuple(list[Tags], list[Items]):
  '''Fetch data, then store it'''

  query_res = query_all_nodes_caen()
  for key, item in query_res.items():
    ...


