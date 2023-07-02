import numpy as np

with open('input16.txt', 'r') as input:
    
    aunts = input.readlines()

check = """
        children: 3
        cats: 7
        samoyeds: 2
        pomeranians: 3
        akitas: 0
        vizslas: 0
        goldfish: 5
        trees: 3
        cars: 2
        perfumes: 1
        """

x_index = {}

for x, line in enumerate(check.split('\n')):
    if ':' in line:
        line = line.replace(' ', '')
        x_index[line[:line.index(':')]] = x - 1


table = np.zeros((len(aunts), len(x_index)), dtype = np.int32) - 1

for x, line in enumerate(aunts):
    line = line[line.index(':') + 2:].replace(' ', '')
    for item in line.split(','):
        table[x, x_index[item[:item.index(':')]]] = int(item[item.index(':') + 1:])

check_vector = np.zeros(len(x_index), dtype = np.int32)

for x, line in enumerate(check.split('\n')):
    if ':' in line:
        line = line.replace(' ', '')
        check_vector[x_index[line[:line.index(':')]]] = int(line[line.index(':') + 1:])

for y, line in enumerate(table):
    if False not in [entry == -1 or entry == check_vector[x] for x, entry in enumerate(line)]:
        print(y+1)
