import os
from time import sleep
from threading import Thread
from typing import Callable

from src.consts import CACHE_DIR, CACHE_FILE_COMPUTED_NODES_DATA, CACHE_FILE_COMPUTED_NODES_REL, CACHE_FILE_COMPUTED_TAGS_DATA, CACHE_FILE_COMPUTED_WAYS_DATA, CACHE_FILE_COMPUTED_WAYS_NAME, CACHE_FILE_COMPUTED_WAYS_WAYS, CACHE_FILE_NODES, CACHE_FILE_WAYS, LOG_DIR, PROJECT_NAME, VERSION



def verify_integrity_cache() -> bool:
  '''Check there is a folder named .cache'''

  # If there is already a FILE named .cache
  if os.path.isfile(CACHE_DIR):
    raise FileExistsError

  # Create directory
  if not os.path.isdir(CACHE_DIR):
    os.makedirs(CACHE_DIR)

  if os.path.isfile(LOG_DIR):
    raise FileExistsError

  if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

  # Check all cache has been built
  return \
    os.path.isfile(CACHE_FILE_WAYS) and \
    os.path.isfile(CACHE_FILE_NODES) and \
    os.path.isfile(CACHE_FILE_COMPUTED_NODES_DATA) and \
    os.path.isfile(CACHE_FILE_COMPUTED_NODES_REL) and \
    os.path.isfile(CACHE_FILE_COMPUTED_WAYS_DATA) and \
    os.path.isfile(CACHE_FILE_COMPUTED_WAYS_WAYS) and \
    os.path.isfile(CACHE_FILE_COMPUTED_WAYS_NAME) and \
    os.path.isfile(CACHE_FILE_COMPUTED_TAGS_DATA) \


def print_version() -> None:
  '''Print the version of the project name'''
  print(f'{PROJECT_NAME} - {VERSION}')


def keys_to_int(x: dict[str, str]):
  '''Convert a key of a json object to an int'''
  return {int(k): v for k, v in x if k.isdigit()}


def thread_me(fn: Callable) -> Callable:
  '''Thread a function, to run in background'''

  def thread(*args) -> None:

    def loop() -> None:
      while True:
        fn(*args)
        sleep(2)

    Thread(target=loop).start()

  return thread

