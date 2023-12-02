
with open('input1.txt', 'r') as input:
    
    lines = input.readlines()

result = 0

def find_digit(string):
    
    for symbol in string:
        if symbol.isnumeric():
            return int(symbol)
        
    return None


for line in lines:
    line_val = 10 * find_digit(line) + find_digit(line[::-1])
    result += line_val

print(result)