import os


CACHE_DIR = os.path.join(os.getcwd(), '.cache')
LOG_DIR = os.path.join(CACHE_DIR, 'logs')

LOG_FILE = os.path.join(CACHE_DIR, 'log.jsonl')
CACHE_FILE_WAYS_CAR = os.path.join(CACHE_DIR, 'ways_car.json')
CACHE_FILE_WAYS_ALL = os.path.join(CACHE_DIR, 'ways_all.json')
CACHE_FILE_NODES = os.path.join(CACHE_DIR, 'nodes.json')
