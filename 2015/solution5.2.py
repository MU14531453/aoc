with open('input5.txt', 'r') as input:

    words = input.readlines()
    
count = 0

def line_check(line: str):

    pairs = [line[i:i+2] for i in range(len(line) - 1)][:-1:]
    triples = [line[i:i+3] for i in range(len(line) - 2)][:-1:]
    
    if not any([triple for triple in triples if triple[0] == triple[2]]):
        return 0
    
    for x, pair in enumerate(pairs):
        temp = [set(x) for x in pairs[0:x] + pairs[x + 1:]]
        if temp.count(set(pair)) > 1:
            return 1

    return 0

# line_check(words[0])
for word in words:
    count += line_check(word)

print(count)
