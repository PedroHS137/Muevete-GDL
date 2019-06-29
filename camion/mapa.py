import gmaps,requests,json
import googlemaps
source = input().replace(' ','+')
dest = input().replace(' ','+')
API_KEY='AIzaSyDX4z2ZEtxzarTUC9NrIdQ61nSczVvr_L8'

# Requires API key
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

# Get method of requests module
# return response object
#r = requests.get(url + 'origins = ' + source +'&destinations = ' + dest + '&key = ' + API_KEY)
#x = r.json()
# bydefault driving mode considered
# print the vale of x

gmaps = googlemaps.Client(API_KEY)

# Requires cities name
my_dist = gmaps.distance_matrix(source, dest)['rows'][0]['elements'][0]

# Printing the result
print(my_dist)
#print(x)