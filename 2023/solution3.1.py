
with open('input3.txt', 'r') as input:

    grid = input.readlines()

y_len = len(grid) - 2
x_len = len(grid[0]) - 2


def around(_y, _x):

    global x_len
    global y_len

    result = []

    for w in range(_y - 1, _y + 2):
        for h in range(_x - 1, _x + 2):
            result.append((w, h))
    
    for i, coord in enumerate(result):
        result[i] = min(x_len, max(0, coord[0])), min(y_len, max(0, coord[1]))
    
    return result


def isvalid(character):
    return True if not(character.isnumeric()) and character != '.' and character != '\n' else False


result = 0

str_buffer = ''
valid_flag = False

for y, line in enumerate(grid):
    for x, symbol in enumerate(line):
        if symbol.isnumeric():
            str_buffer += symbol
            if any([isvalid(grid[i[0]][i[1]]) for i in around(y, x)]):
                valid_flag = True
        else:
            if valid_flag:
                result += int(str_buffer)
                valid_flag = False
                str_buffer = ''
            else:
                str_buffer = ''

print(result)