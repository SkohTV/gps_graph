import json
import heapq
from collections import defaultdict
from difflib import SequenceMatcher as SM
import operator

from src.consts import CACHE_FILE_COMPUTED_TAGS_DATA
from src.logging import logger
from src.graph.utils import normalize_string
from src.graph.types import Key
from src.graph.nodes import DictNodes



class TagsDict:
  '''Represent a dict of tags, linking to matching locations'''

  def __init__(self, dict_nodes: DictNodes) -> None:
    self._data: dict[Key, str] = dict()
    self._dict_nodes: DictNodes = dict_nodes


  def generate_tags_dict(self) -> None:
    '''Generate a list of tags from a fully loaded DictNodes'''
    self._data = {k: normalize_string(' '.join(v[2])) for k, v in self._dict_nodes._data.items()}


  def search_for_tags(self, string: str) -> list[Key]:
    '''Search for the node with the tags closest matching the string'''
    word = normalize_string(string)
    scores = [(k, SM(None, word, v).ratio()) for k, v in self._data.items()]
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = [(k, sc, self._data[k]) for k, sc in scores]
    print(json.dumps(scores))
    # return [k for k, _ in scores][:10]



  def save_to_file(self) -> None:
    '''Save the big data to files to avoid recompute'''
    logger.info('Saving tags_data to file')
    with open(CACHE_FILE_COMPUTED_TAGS_DATA, 'w') as f:
      json.dump(self._data, f)


  def load_from_file(self) -> None:
    '''Load the big data from the cached json'''
    logger.info('Loading tags_data from file')
    with open(CACHE_FILE_COMPUTED_TAGS_DATA) as f:
      self._data = json.load(f)

