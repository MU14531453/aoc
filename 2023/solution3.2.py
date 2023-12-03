
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

result = 0

for y, line in enumerate(grid):
    for x, symbol in enumerate(line):
        if symbol == '*':
            gear = (y, x)
            line_up = grid[y-1]
            line_down = grid[y+1]
            line_left = line[:x]
            line_right = line[x+1:]

            ratio = []
            str_buffer = ''
            valid_flag = False
            for w, symbol_ in enumerate(line_up):
                if symbol_.isnumeric():
                    str_buffer += symbol_
                    if gear in around(y-1, w):
                        valid_flag = True
                else:
                    if valid_flag:
                        ratio.append(int(str_buffer))
                        str_buffer = ''
                        valid_flag = False
                    else:
                        str_buffer = ''

            for w, symbol_ in enumerate(line_down):
                if symbol_.isnumeric():
                    str_buffer += symbol_
                    if gear in around(y+1, w):
                        valid_flag = True
                else:
                    if valid_flag:
                        ratio.append(int(str_buffer))
                        str_buffer = ''
                        valid_flag = False
                    else:
                        str_buffer = ''

            if line_left[-1].isnumeric():
                for w, digit in enumerate(line_left[::-1]):
                    if digit.isnumeric():
                        str_buffer += digit
                    else:
                        break
                ratio.append(int(str_buffer[::-1]))
                str_buffer = ''
                
            if line_right[0].isnumeric():
                for w, digit in enumerate(line_right):
                    if digit.isnumeric():
                        str_buffer += digit
                    else:
                        break
                ratio.append(int(str_buffer))
                str_buffer = ''
            
            if len(ratio) == 2:
                result += ratio[0] * ratio[1]
            ratio = []
            
print(result)
