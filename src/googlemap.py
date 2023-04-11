#AIzaSyACHjIhw1jMpcIOUYLepvTWbNgfw7gEhu0
import googlemaps
import networkx as nx
import matplotlib.pyplot as plt

# Set up Google Maps API client
gmaps = googlemaps.Client(key='AIzaSyACHjIhw1jMpcIOUYLepvTWbNgfw7gEhu0')

# Set up empty graph
G = nx.Graph()

# Define coordinates for each location
coords = {'A': (-6.882008, 107.610173),
          'B': (-6.893611, 107.604807),
          'C': (-6.902092, 107.638645),
          'D': (-6.890838, 107.609777),
          'E': (-6.887477, 107.609442),
          'F': (-6.886329, 107.610323),
          'G': (-6.874570, 107.602827),
          'H': (-6.865918, 107.603324)}

# Calculate distances between locations and add edges to graph
for i, loc1 in enumerate(coords.keys()):
    for loc2 in list(coords.keys())[i+1:]:
        # Get coordinates of locations
        coord1 = coords[loc1]
        coord2 = coords[loc2]
        # Calculate Euclidean distance between locations
        dist = ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5
        # Add edge to graph
        G.add_edge(loc1, loc2, weight=dist)

# Set up figure and draw map
fig, ax = plt.subplots()
with open('map.html', 'w') as f:
    f.write('<iframe width="800" height="600" src="https://www.google.com/maps/embed/v1/directions?origin=')
    for loc, coord in coords.items():
        f.write(str(coord[0]) + ',' + str(coord[1]) + '&destination=')
        ax.annotate(loc, coord[::-1])
    f.seek(f.tell()-13)
    f.write('&key=your_API_key"></iframe>')
    ax.imshow(plt.imread(f.name), extent=[107.58, 107.65, -6.91, -6.86])

# Draw graph
pos = {loc: coord[::-1] for loc, coord in coords.items()}
nx.draw(G, pos, with_labels=True, font_weight='bold', ax=ax)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
plt.show()
