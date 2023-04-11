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
print("Cost: ", ucs_cost)
drawGraph(dist,ucs_path, matrix)
print("Displaying graph for A* Algorithm...")
print("...")
print("Cost: ", as_cost)
drawGraph(dist, as_path, matrix)