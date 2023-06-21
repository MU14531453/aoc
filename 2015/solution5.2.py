from copy import deepcopy

with open('input5.txt', 'r') as input:

    words = input.readlines()

count = 0

def line_check(line: str):

    pairs = [line[i:i+2] for i in range(len(line)-1)][:-1:]
    triples = [line[i:i+3] for i in range(len(line) - 1)][:-1:]
    if not any([triple for triple in triples if triple[0] == triple[2]]):
        return 0

    for x, pair in enumerate(pairs):
        pairs_check = deepcopy(pairs)
        pairs_check[max(0,x-1)] = pairs_check[x] = pairs_check[min(x+1, len(pairs_check)-1)] = '000'
        
        if any([pair == x for x in pairs_check]):
            return 1

    return 0

for word in words:
    count += line_check(word)

print(count)
