import argparse
from functools import cache


@cache
def setup_parser() -> argparse.Namespace:
  '''Init the parser with correct params'''
  parser = argparse.ArgumentParser(
    prog='GPS Graph',
    description='Blablabla',
  )

  parser.add_argument('-e', '--env', metavar='FILE', help='pick a file to load environnement variables from (for iCloud credentials)')
  parser.add_argument('--version', action='store_true', help='show the version of the software then exit')
  parser.add_argument('-v', '--verbose', action='store_true', help='enable all debug logs')
  parser.add_argument('-n', '--no-gui', action='store_true', help='do not open the gui window')
  parser.add_argument('-s', '--silent', action='store_true', help='silence output')
  parser.add_argument('--force-rebuild-cache', action='store_true', help='force the rebuild of the cached jsons')
  return parser.parse_args()


arguments = setup_parser()
