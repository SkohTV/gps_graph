from src.core.mapping import testing_loadall_nodes
from src.args import setup_parser
from src.logging import logger
from src.core import verify_integrity_cache
from src.logging import setup_logging
from src.api import load_cache, update_cache
from src.args import arguments
from src.gui.app import App
from src.app import main


if __name__ == "__main__":
  # main()

  # logger.debug("debug message", extra={"x": "hello"})
  # logger.info("info message")
  # logger.warning("warning message")
  # logger.error("error message")
  # logger.critical("critical message")

  app = App()
  app.mainloop()