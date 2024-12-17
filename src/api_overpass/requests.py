# AREA_ID = '3600149197' # Caen
AREA_ID = '3600007453' # Calvados
# AREA_ID = '3603793170' # Normandy


TIMEOUT = 25


QUERY_NODES = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  (
    nwr["addr:housenumber"](area.searchArea);
    nwr["type"="associatedStreet"](area.searchArea);

    nwr["shop"](area.searchArea);
    nwr["brand"](area.searchArea);
  );
  out geom;
'''
# nwr["amenity"](area.searchArea);


QUERY_WAYS = f'''\
  [out:json][timeout:{TIMEOUT}];
  area(id:{AREA_ID})->.searchArea;
  nwr["highway"](area.searchArea);
  out geom;
'''
