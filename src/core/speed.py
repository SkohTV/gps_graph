from src.graph.types import MaxSpeed


def get_speed(highway: str) -> MaxSpeed:
  '''
  Convert the highway type into the speed limit of this type of road
  https://wiki.openstreetmap.org/wiki/Key:highway
  '''

  match highway:
    case 'residential':
      return (50, 15, 4)
    case 'motorway':
      return (130, 1, 1)
    case 'trunk':
      return (80, 15, 1)
    case 'primary':
      return (80, 15, 1)
    case 'secondary':
      return (80, 15, 1)
    case 'tertiary':
      return (70, 15, 1)
    case 'unclassified':
      return (50, 15, 4)
    case 'motorway_link':
      return (130, 1, 1)
    case 'trunk_link':
      return (80, 15, 1)
    case 'primary_link':
      return (80, 15, 1)
    case 'secondary_link':
      return (80, 15, 1)
    case 'tertiary_link':
      return (70, 15, 1)
    case 'living_street':
      return (10, 15, 4)
    case 'service':
      return (0, 15, 4)
    case 'pedestrian':
      return (0, 15, 4)
    case 'track':
      return (0, 15, 4)
    case 'bus_guideway':
      return (10, 15, 4)
    case 'escape':
      return (10, 1, 1)
    case 'road':
      return (90, 15, 4)
    case 'busway':
      return (0, 1, 1)
    case 'footway':
      return (0, 15, 4)
    case 'bridleway':
      return (0, 15, 4)
    case 'steps':
      return (0, 1, 4)
    case 'path':
      return (0, 15, 4)
    case 'sidewalk':
      return (0, 1, 4)
    case 'crossing':
      return (0, 1, 4)
    case 'traffic_island':
      return (0, 1, 4)
    case 'cycleway':
      return (0, 15, 4)
    case 'lane':
      return (0, 15, 1)
    case 'opposite':
      return (0, 15, 4)
    case 'opposite_lane':
      return (0, 15, 4)
    case 'track':
      return (0, 15, 4)
    case 'opposite_track':
      return (0, 15, 4)
    case 'share_busway':
      return (0, 15, 1)
    case 'opposite_share_busway':
      return (0, 15, 1)
    case 'shared_lane':
      return (0, 15, 1)
    case 'construction':
      return (0, 1, 1)
    case _:
      return (90, 15, 4)


