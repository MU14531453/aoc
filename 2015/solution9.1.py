from copy import copy
import numpy as np

with open('input9.txt', 'r') as input:
    
    paths = input.readlines()

distances = [path[:-1].replace(' to ', ' = ').split(' = ') for path in paths]

places = []
for dist in distances:
    places.append(dist[0])
    places.append(dist[1])
places = list(set(places))

# Too poor to afford importing pandas
table = np.zeros((len(places), len(places)), dtype = np.int32 )
indexes = {x : places.index(x) for x in places}

for distance in distances:
    table[indexes[distance[0]]][indexes[distance[1]]] = int(distance[2])
    table[indexes[distance[1]]][indexes[distance[0]]] = int(distance[2])

paths = []

for x, start in enumerate(places[0:]):
    
    pathlen = 0
    c_table = np.copy(table)
    
    while np.sum(c_table) > 0:
        
        row = table[x,...]
        newdist = row[row > 0].min()
        
        pathlen += newdist
        x = np.where(row == newdist)
        c_table[...,x] = 0
        print(c_table)




    paths.append(pathlen)

print(paths)