import os


PROJECT_NAME = 'gps_graph' # Yes, this is a modular value
VERSION = '0.0.1-dev'

CACHE_DIR = os.path.join(os.getcwd(), '.cache')
LOG_DIR = os.path.join(CACHE_DIR, 'logs')

LOG_FILE = os.path.join(CACHE_DIR, 'log.jsonl')
CACHE_FILE_WAYS = os.path.join(CACHE_DIR, 'ways.json')
CACHE_FILE_NODES = os.path.join(CACHE_DIR, 'nodes.json')

VALID_TAGS = [
  'addr:housenumber',
  'addr:street'
]
