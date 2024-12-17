import json
from difflib import SequenceMatcher as SM

from src.consts import CACHE_FILE_COMPUTED_TAGS_DATA
from src.logging import logger
from src.graph.utils import normalize_string
from src.graph.types import Key
from src.graph.nodes import DictNodes
from src.utils import keys_to_int



class TagsDict:
  '''Represent a dict of tags, linking to matching locations'''

  def __init__(self, dict_nodes: DictNodes) -> None:
    self._data: dict[Key, str] = dict()
    self._dict_nodes: DictNodes = dict_nodes


  def _super_normalize(self, kw: str) -> str:
    return '-'.join(sorted([normalize_string(x) for x in kw.replace(' ', '-').split('-')]))


  def generate_tags_dict(self) -> None:
    '''Generate a list of tags from a fully loaded DictNodes'''
    self._data = {
      k: '-'.join([self._super_normalize('-'.join(v[2]))])
      for k, v in self._dict_nodes._data.items()
    }


  def search_for_tags(self, string: str) -> list[Key]:
    '''Search for the node with the tags closest matching the string'''
    word = self._super_normalize(string)
    scores = [(k, SM(None, word, v).quick_ratio()) for k, v in self._data.items()]
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = [(k, sc) for k, sc in scores]
    return [k for k, _ in scores][:10]


  def save_to_file(self) -> None:
    '''Save the big data to files to avoid recompute'''
    logger.info('Saving tags_data to file')
    with open(CACHE_FILE_COMPUTED_TAGS_DATA, 'w') as f:
      json.dump(self._data, f)


  def load_from_file(self) -> None:
    '''Load the big data from the cached json'''
    logger.info('Loading tags_data from file')
    with open(CACHE_FILE_COMPUTED_TAGS_DATA) as f:
      self._data = json.load(f, object_pairs_hook=keys_to_int) # type: ignore

