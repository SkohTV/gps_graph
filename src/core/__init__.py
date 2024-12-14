from __future__ import annotations
from dataclasses import dataclass
import os

from src.consts import CACHE_DIR, LOG_DIR


@dataclass
class Tag:
  name: str
  list: Item


@dataclass
class Item:
  name: str
  list: Tag


# Check quad tree
# def build_items_tags() -> tuple(list[Tags], list[Items]):
#   '''Fetch data, then store it'''
#
#   query_res = query_all_nodes_caen()
#   for key, item in query_res.items():
#     ...


def verify_integrity_cache() -> None:
  '''Check there is a folder named .cache'''

  # If there is already a FILE named .cache
  if os.path.isfile(CACHE_DIR):
    raise FileExistsError

  # Create directory
  if not os.path.isdir(CACHE_DIR):
    os.makedirs(CACHE_DIR)

  if os.path.isfile(LOG_DIR):
    raise FileExistsError

  if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

