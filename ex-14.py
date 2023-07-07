#Distance between Kyiv and London

import math

RADIUS = 6371.01 #radius of Earth

lat1 = math.radians(50.45) #coordinates of Kyiv conveted in radians
lon1 = math.radians(30.523)

lat2 = math.radians(51.5072) #coordinates of London conveted in radians
lon2 = math.radians(-0.1275)

#Calculation of distance
distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1-lon2))