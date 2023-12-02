
with open('input2.txt', 'r') as input:

    lines = input.readlines()

result = 0

def get_power(string):

    min_cubes = {}
    min_cubes['red'] = 0
    min_cubes['green'] = 0
    min_cubes['blue'] = 0

    string = string.split(': ')[1].replace(',', ';').replace('; ', ';').split(';')
    
    for sub_game in string:
        value, register = sub_game.split(' ')[0], sub_game.split(' ')[1]
        min_cubes[register] = max(min_cubes[register], int(value))

    return min_cubes['red']*min_cubes['green']*min_cubes['blue']

for line in lines:
    result += get_power(line[:-1])

print(result)