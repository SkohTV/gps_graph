# AREA_ID = '3600149197' # Caen
AREA_ID = '3600007453' # Calvados
TIMEOUT = 25

CAR_HIGHWAYS = [
  'motorway',
  'trunk',
  'primary',
  'secondary',
  'tertiary',
  'unclassified',
  'residential',
  'motorway_link',
  'trunk_link',
  'primary_link',
  'secondary_link',
  'tertiary_link',
  'living_street',
]

WALK_BIKE_WAYS = [

]


QUERY_NODES = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["amenity"](area.searchArea);
  nwr["addr:housenumber"](area.searchArea);
  out geom;
'''

# https://wiki.openstreetmap.org/wiki/Key:highway
QUERY_WAYS_ALL = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["highway"~"{'|'.join(CAR_HIGHWAYS)}"](area.searchArea);
  out geom;
'''

QUERY_WAYS_ALL = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["highway"~"{'|'.join(WALK_BIKE_WAYS)}"](area.searchArea);
  out geom;
'''
