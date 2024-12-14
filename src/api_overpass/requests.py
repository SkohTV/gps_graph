# AREA_ID = '3600149197' # Caen
AREA_ID = '3600007453' # Calvados
TIMEOUT = 25


# https://wiki.openstreetmap.org/wiki/Key:highway
CAR_HIGHWAYS = [

]


QUERY_NODES = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["amenity"](area.searchArea);
  nwr["addr:housenumber"](area.searchArea);
  out geom;
'''

QUERY_WAYS = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["highway"](area.searchArea);
  out geom;
'''
