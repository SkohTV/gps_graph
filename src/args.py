import argparse
from functools import cache


@cache
def setup_parser() -> argparse.Namespace:
  '''Init the parser with correct params'''
  parser = argparse.ArgumentParser(
    prog='GPS Graph',
    description='Blablabla',
  )

  parser.add_argument('-v', '--verbose', action='store_true')
  parser.add_argument('-n', '--no-gui', action='store_true')
  parser.add_argument('-s', '--silent', action='store_true')
  parser.add_argument('--force-rebuild-cache', action='store_true')
  return parser.parse_args()


arguments = setup_parser()
