from pyicloud import PyiCloudService

from src.graph.types import Position
from src.logging import logger



class Icloud:
  '''
  Represent an iCloud connection to an iPhone, to get GPS data
  This is not the ideal way to do this
  So we will assume a lot of things to avoid working with
  Weird and numerous edge cases
  '''

  def __init__(self) -> None:
    '''Create empty attributes to store logged in data'''
    self.api = None
    self.iphone = None


  def login(self, email: str, pwd: str) -> bool:
    '''Send a login request to the icloud account'''

    if not email or not pwd:
      logger.error('No iCloud email or password')
      return False

    self.api = PyiCloudService(email, pwd)

    if self.api.requires_2fa:
      logger.info('2fa required, enter code : ')
      code = input()
      result = self.api.validate_2fa_code(code)
      logger.debug(f'Code validation status is {result}')

      if not result:
        logger.error("Failed to verify security code")
        return False

    if not self.api.is_trusted_session:
      logger.info('Session not trusted, requesting trust')
      result = self.api.trust_session()
      logger.debug(f'Session trust status is {result}')

      if not result:
        logger.error('Failed to request trust')
        return False

    # We do not handle 2sa because idk what it is and don't wanna bother with it
    # We also assume that the user will ONLY log in with an iPhone
    # I can't test with another one because I don't have another one
    # So let's not bother

    self.iphone = self.api.devices[0]

    return True


  # To verify : https://gps-coordinates.org/
  def gps_request(self) -> Position:
    '''Send a GPS request to the logged in iPhone, and return the lat and longitude'''

    # If we call this before self.login() or self.login() failed
    if self.iphone is None:
      logger.error('No iPhone logged in')
      raise RuntimeError

    loc = self.iphone.location()
    return (loc["latitude"], loc["longitude"])

