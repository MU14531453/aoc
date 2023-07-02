from copy import copy
import numpy as np

with open('input9.txt', 'r') as input:
    
    paths = input.readlines()

distances = [path[:-1].replace(' to ', ' = ').split(' = ') for path in paths]

distances_array = np.zeros(shape = (8,8), dtype = np.int32)

places = []

for path in distances:
    if path[0] not in places:
        places.append(path[0])
    if path[1] not in places:
        places.append(path[1])

for path in distances:
    x = places.index(path[0])
    y = places.index(path[1])
    distances_array[x][y] = distances_array[y][x] = int(path[2])


def dijkstra(graph: np.ndarray):
    pass