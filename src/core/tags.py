import json
from difflib import SequenceMatcher as SM

from src.consts import CACHE_FILE_COMPUTED_TAGS_DATA
from src.logging import logger
from src.graph.utils import normalize_string
from src.graph.types import Key
from src.graph.nodes import DictNodes



class TagsDict:
  '''Represent a dict of tags, linking to matching locations'''

  def __init__(self, dict_nodes: DictNodes) -> None:
    self._data: dict[str, list[Key]] = dict()
    self._dict_nodes: DictNodes = dict_nodes


  def generate_tags_dict(self) -> None:
    '''Generate a list of tags from a fully loaded DictNodes'''

    for key, (_, _, tags) in self._dict_nodes._data.items():

      for tag in tags:
        if tag in self._data:
          self._data[tag].append(key)
        else:
          self._data[tag] = [key]


  def search_for_tags(self, string: str) -> list[Key]:
    string = normalize_string(string)
    scores = [(SM(None, string, k).ratio(), v) for k, v in self._data.items()]
    scores.sort(key=lambda x: x[0])

    res = []
    break_outer = False

    for s in scores:
      for n in s[1]:
        res.append(n)

        if len(res) >= 10:
          break_outer = True
          break

      if break_outer: break

    return res


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

