import math
from astar import *
from ucs import *
from iofile import *
from visgraph import *
import googlemaps

def distance(arg1,arg2):
    return math.sqrt((arg1[0]-arg1[1])**2 + (arg1[1]-arg2[1])**2)

filename = input("Filename (in .txt): ")
matrix, koordinat = readFile(filename)

n_points = len(koordinat)
dist = []

for i in range(n_points):
    tmpdist = []
    for j in range(n_points):
        tmpdist.append(distance(koordinat[i],koordinat[j]))
    dist.append(tmpdist)

start = int(input("Starting point: "))
end = int(input("Target point: "))

ucs_cost, ucs_path = ucs(dist, matrix,start,end)

as_totalcost, as_cost, as_path = astar(dist, matrix ,start, end)

print("Displaying graph for UCS Algorithm...")
print("...")
drawGraph(dist,ucs_path, matrix)
print("Displaying graph for A* Algorithm...")
print("...")
drawGraph(dist, as_path, matrix)

print(as_path)
gmaps = googlemaps.Client(key='AIzaSyACHjIhw1jMpcIOUYLepvTWbNgfw7gEhu0')

G = nx.Graph()

coords = {}

def add_coords(key, lat, long):
    coords[key] = (lat,long)

for i in range(len(as_path)):
    if (i == 1):
        add_coords(chr(i+65),koordinat[as_path[len(as_path)-1]][0],koordinat[as_path[len(as_path)-1]][1])
    elif (i>1):
        add_coords(chr(i+65),koordinat[as_path[i-1]][0],koordinat[as_path[i-1]][1])
    else:
        add_coords(chr(i+65),koordinat[as_path[i]][0],koordinat[as_path[i]][1])
 
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
    f.write('&key=AIzaSyACHjIhw1jMpcIOUYLepvTWbNgfw7gEhu0"></iframe>')
    ax.imshow(plt.imread(f.name), extent=[107.58, 107.65, -6.91, -6.86])

# Draw graph
pos = {loc: coord[::-1] for loc, coord in coords.items()}
nx.draw(G, pos, with_labels=True, font_weight='bold', ax=ax)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
plt.show()