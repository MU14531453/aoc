
with open('input2.txt', 'r') as input:

    lines = input.readlines()

max_cubes = {}
max_cubes['red'] = 12
max_cubes['green'] = 13
max_cubes['blue'] = 14

result = 0

def check_validity(string):

    string = string.split(': ')[1].replace(',', ';').replace('; ', ';')

    for draw in string.split(';'):
        if max_cubes[draw.split(' ')[1]] < int(draw.split(' ')[0]):
            return False

    return True


for x, line in enumerate(lines):
    if check_validity(line[:-1]):
        result += x + 1
    
print(result)