#! /usr/bin/env python

# # original start and end (straight line)
# lat1 = 33.75534
# lon1 = -84.42820
# lat2 = 33.75613
# lon2 = -84.42804

# # two intersections
# lat1 = 33.75504 # start at Orleander St NW
# lon1 = -84.42803
# lat2 = 33.75690
# lon2 = -84.42821

# make a right at Gardenia St NW
lat1 = 33.75534 # start between Orleander and Gardenia
lon1 = -84.42820
lat2 = 33.75592
lon2 = -84.42776

# # make a right at Lena St NW
# lat1 = 33.75534 # start between Orleander and Gardenia
# lon1 = -84.42820
# lat2 = 33.75672
# lon2 = -84.42772

url = 'http://127.0.0.1:5000/route/v1/driving/' + str(lon1) + ',' + str(lat1) + ';' + str(lon2) + ',' + str(lat2) + '?steps=true&geometries=geojson'

print str(url)
