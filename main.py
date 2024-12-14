from src.core.mapping import testing_loadall_nodes
from src.args import setup_parser
from src.logging import logger
from src.core import verify_integrity_cache
from src.logging import setup_logging
from src.api import load_cache, update_cache
from src.args import arguments



def main():
  verify_integrity_cache() # Check the .cache folder is valid
  setup_parser() # Init the parser
  setup_logging() # Init the logger

  # Rebuild cache depending on args
  update_cache(force=arguments.force_rebuild_cache)

  load_cache() # Load the cached files

  if not arguments.no_gui:
    # run gui
    ...

  logger.debug('Reached end of script, goodbye')



if __name__ == "__main__":
  main()

  testing_loadall_nodes()

  # logger.debug("debug message", extra={"x": "hello"})
  # logger.info("info message")
  # logger.warning("warning message")
  # logger.error("error message")
  # logger.critical("critical message")

