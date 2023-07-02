import numpy as np

with open('input16.txt', 'r') as input:
    
    aunts = input.readlines()

for line in aunts[0]:
    line = line[line.index(':'):]
    print(line)

clues = np.empty()