import os

from src.consts import CACHE_DIR, LOG_DIR, PROJECT_NAME, VERSION



def verify_integrity_cache() -> None:
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


def print_version() -> None:
  print(f'{PROJECT_NAME} - {VERSION}')
