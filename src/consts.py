import os


PROJECT_NAME = 'gps_graph' # Yes, this is a modular value
VERSION = '0.0.1-dev'

CACHE_DIR = os.path.join(os.getcwd(), '.cache')
LOG_DIR = os.path.join(CACHE_DIR, 'logs')

LOG_FILE = os.path.join(CACHE_DIR, 'log.jsonl')
CACHE_FILE_WAYS = os.path.join(CACHE_DIR, 'ways.json')
CACHE_FILE_NODES = os.path.join(CACHE_DIR, 'nodes.json')

CACHE_FILE_COMPUTED_NODES_DATA = os.path.join(CACHE_DIR, 'computed_nodes_data.json')
CACHE_FILE_COMPUTED_NODES_REL = os.path.join(CACHE_DIR, 'computed_nodes_rel.json')
CACHE_FILE_COMPUTED_WAYS_DATA = os.path.join(CACHE_DIR, 'computed_ways_data.json')
CACHE_FILE_COMPUTED_WAYS_WAYS = os.path.join(CACHE_DIR, 'computed_ways_ways.json')
CACHE_FILE_COMPUTED_WAYS_NAME = os.path.join(CACHE_DIR, 'computed_ways_name.json')
CACHE_FILE_COMPUTED_TAGS_DATA = os.path.join(CACHE_DIR, 'computed_tags_data.json')

