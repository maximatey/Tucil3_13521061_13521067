#AIzaSyACHjIhw1jMpcIOUYLepvTWbNgfw7gEhu0
import googlemaps
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image

# Set up Google Maps API client
gmaps = googlemaps.Client(key='AIzaSyACHjIhw1jMpcIOUYLepvTWbNgfw7gEhu0')

# Set up empty graph
G = nx.Graph()

# Set up map size and zoom level
size = '800x600'
zoom = 14

# Set up markers list
markers = []

# Loop to add nodes to the graph by clicking on the map
print('Add nodes to the graph by clicking on the map (press q to quit)...')
while True:
    # Get user input for node location
    loc = input('Enter node name: ')
    if loc == 'q':
        break
    lat, lng = input('Enter location (lat,lng): ').split(',')
    lat, lng = float(lat), float(lng)
    # Add node to the graph
    G.add_node(loc, pos=(lat, lng))
    markers.append('markers=color:red%7Clabel:{}%7C{},{}'.format(loc, lat, lng))
    print('Node added to graph!')

# Loop to add edges to the graph
print('Add edges to the graph by clicking on the map (press q to quit)...')
while True:
    # Get user input for edge endpoints
    loc1 = input('Enter node 1: ')
    if loc1 == 'q':
        break
    loc2 = input('Enter node 2: ')
    if loc2 == 'q':
        break
    # Add edge to the graph
    dist = gmaps.distance_matrix((G.nodes[loc1]['pos'], G.nodes[loc2]['pos']), mode='walking')['rows'][0]['elements'][0]['distance']['value']
    G.add_edge(loc1, loc2, weight=dist)
    print('Edge added to graph!')

# Draw graph
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Display map using Google Maps Static API
url = 'https://maps.googleapis.com/maps/api/staticmap?size={}&maptype=roadmap&path='.format(size)
path = 'color:blue|weight:5|enc:'
for i, node in enumerate(G.nodes):
    if i == 0:
        path += gmaps.reverse_geocode(G.nodes[node]['pos'])[0]['formatted_address']
    path += '{},{}|'.format(G.nodes[node]['pos'][0], G.nodes[node]['pos'][1])
markers.append('markers=color:green%7C{}'.format(path[:-1]))
url += path[:-1] + '&' + '&'.join(markers) + '&key=your_API_key'
img = np.array(Image.open(urllib.request.urlopen(url)))
plt.imshow(img)
plt.show()

