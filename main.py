from src.args import setup_parser
from src.logging import logger
from src.core import verify_integrity_cache
from src.logging import setup_logging
from src.api_requests import update_cache_map
from src.args import arguments



def main():
  verify_integrity_cache()
  setup_parser()
  setup_logging()
  update_cache_map()


if __name__ == "__main__":
  main()


  logger.debug("debug message", extra={"x": "hello"})
  logger.info("info message")
  logger.warning("warning message")
  logger.error("error message")
  logger.critical("critical message")
