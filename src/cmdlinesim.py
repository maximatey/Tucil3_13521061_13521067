import math
from astar import *
from ucs import *
from iofile import *
from visgraph import *

def distance(arg1,arg2):
    return math.sqrt((arg1[0]-arg1[1])**2 + (arg1[1]-arg2[1])**2)

filename = input("Filename (in .txt)): ")
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

# print(ucs_cost)
# print(ucs_path)
# print(as_path)
# print(as_cost)

if as_cost > ucs_cost: 
    drawGraph(matrix,ucs_path)
else:
    drawGraph(matrix,as_path)