import os

from dotenv import load_dotenv

from src.core.tags import TagsDict
from src.graph.nodes import DictNodes
from src.graph.ways import GraphWays
from src.api_icloud import Icloud
from src.args import setup_parser
from src.logging import logger
from src.utils import verify_integrity_cache
from src.logging import setup_logging
from src.api_overpass import load_web_cache, update_cache
from src.args import arguments
from src.utils import print_version
from src.gui.app import App




def main():
  '''Main logic for the app'''

  # Print the version then exit
  if arguments.version:
    print_version()
    return

  # Load env vars from .env file
  if arguments.env:
    load_dotenv(arguments.env) 

  verify_integrity_cache() # Check the .cache folder is valid
  setup_parser() # Init the parser
  setup_logging() # Init the logger

  # Login into iCloud
  if not arguments.no_login:
    icloud = Icloud()
    ret = icloud.login(os.getenv('ICLOUD_EMAIL') or '', os.getenv('ICLOUD_PWD') or '')

    # Exit if failed to login
    if not ret:
      logger.error('Failed to login into iCloud, exiting')
      return

  graph_ways = GraphWays()
  dict_nodes = DictNodes(graph_ways=graph_ways)
  tags_dict = TagsDict(dict_nodes=dict_nodes)

  # Rebuild cache depending on args
  if arguments.force_rebuild_cache:
    # update_cache(force=True)

    nodes, ways = load_web_cache()
    graph_ways.load(ways)
    dict_nodes.load(nodes)
    tags_dict.generate_tags_dict()

    graph_ways.save_to_file()
    dict_nodes.save_to_file()
    tags_dict.save_to_file()

  else:
    graph_ways.load_from_file()
    dict_nodes.load_from_file()
    tags_dict.load_from_file()
  

  tags_dict.search_for_tags('hello')


  if not arguments.no_gui:
    app = App()
    app.mainloop()

  logger.debug('Reached end of script, goodbye')

