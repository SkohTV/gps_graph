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
from src.core.bridge import BridgeApi, bridge_api




def main():
  '''Main logic for the app'''
  global bridge_api

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

  # Init the big global var
  _graph_ways = GraphWays()
  _dict_nodes = DictNodes(graph_ways=_graph_ways)
  _tags_dict = TagsDict(dict_nodes=_dict_nodes)
  _icloud = Icloud()
  bridge_api = BridgeApi(g=_graph_ways, d=_dict_nodes, t=_tags_dict, i=_icloud)


  # Login into iCloud
  if not arguments.no_login:
    ret = bridge_api.icloud.login(os.getenv('ICLOUD_EMAIL') or '', os.getenv('ICLOUD_PWD') or '')

    # Exit if failed to login
    if not ret:
      logger.error('Failed to login into iCloud, exiting')
      return


  # Rebuild cache depending on args
  if arguments.force_rebuild_cache:
    # update_cache(force=True)

    nodes, ways = load_web_cache()
    bridge_api.graph_ways.load(ways)
    bridge_api.dict_nodes.load(nodes)
    bridge_api.tags_dict.generate_tags_dict()

    bridge_api.graph_ways.save_to_file()
    bridge_api.dict_nodes.save_to_file()
    bridge_api.tags_dict.save_to_file()

  else:
    bridge_api.graph_ways.load_from_file()
    bridge_api.dict_nodes.load_from_file()
    bridge_api.tags_dict.load_from_file()
  

  bridge_api.get_possible_addresse('Rue Haie Vigné Caen 54')


  # Run the GUI
  if not arguments.no_gui:
    app = App()
    app.mainloop()


  # When the program exit
  logger.debug('Reached end of script, goodbye')

