import os
from dotenv import load_dotenv

from src.api_icloud import Icloud
from src.args import setup_parser
from src.logging import logger
from src.utils import verify_integrity_cache
from src.logging import setup_logging
from src.api_overpass import load_cache, update_cache
from src.args import arguments
from src.utils import print_version



def main():

  if arguments.version:
    print_version()
    return

  if arguments.env:
    load_dotenv(arguments.env) # Load env vars from .env file

  verify_integrity_cache() # Check the .cache folder is valid
  setup_parser() # Init the parser
  setup_logging() # Init the logger

  icloud = Icloud()
  ret = icloud.login(os.getenv('ICLOUD_EMAIL') or '', os.getenv('ICLOUD_PWD') or '')

  # Rebuild cache depending on args
  update_cache(force=arguments.force_rebuild_cache)

  load_cache() # Load the cached files

  if not arguments.no_gui:
    # run gui
    ...

  logger.debug('Reached end of script, goodbye')



# Ne s'exéctue que si main.py est lancé, pas importé
if __name__ == "__main__":
  main()

  # testing_loadall_nodes()

  # logger.debug("debug message", extra={"x": "hello"})
  # logger.info("info message")
  # logger.warning("warning message")
  # logger.error("error message")
  # logger.critical("critical message")

