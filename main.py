import os
from dotenv import load_dotenv

from src.graph.graph_ways import GraphWays
from src.api_icloud import Icloud
from src.args import setup_parser
from src.logging import logger
from src.utils import verify_integrity_cache
from src.logging import setup_logging
from src.api_overpass import load_cache, update_cache
from src.args import arguments
from src.utils import print_version



def main():

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

  # Rebuild cache depending on args
  update_cache(force=arguments.force_rebuild_cache)

  if not arguments.no_gui:
    # run gui
    ...

  nodes, ways = load_cache()

  graph_ways = GraphWays()
  graph_ways.load(ways)

  logger.debug('Reached end of script, goodbye')



if __name__ == "__main__":
  main()

  # testing_loadall_nodes()

  # logger.debug("debug message", extra={"x": "hello"})
  # logger.info("info message")
  # logger.warning("warning message")
  # logger.error("error message")
  # logger.critical("critical message")

