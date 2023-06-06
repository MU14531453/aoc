with open('input5.txt', 'r') as input:
    
    words = input.readlines()
    
count = 0

def line_check(line: str):

    bad_letters = ['ab', 'cd', 'pq', 'xy']
    wovels = ['a', 'e', 'i', 'o', 'u']

    pairs = [line[i:i+2] for i in range(len(line) - 1)][:-1:]
    
    if not any([pair for pair in pairs if pair[0] == pair[1]]):
        return 0

    if any([pair for pair in pairs if pair in bad_letters]):
        return 0

    if len([letter for letter in word if letter in wovels]) < 3:
        return 0
    
    return 1

for word in words:
    count += line_check(word)

print(count)