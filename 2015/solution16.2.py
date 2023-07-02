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
    subresult = []
    for x in range(10):
        if x == 1 or x == 7:
            if line[x] == -1 or line[x] > check_vector[x]:
                subresult.append(True)
            else:
                subresult.append(False)
        elif x == 3 or x == 6:
            if line[x] == -1 or line[x] < check_vector[x]:
                subresult.append(True)
            else:
                subresult.append(False)
        else:
            if line[x] == -1 or line[x] == check_vector[x]:
                subresult.append(True)
            else:
                subresult.append(False)

    if False not in subresult:
        print(y+1)