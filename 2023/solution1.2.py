
with open('input1.txt', 'r') as input:
    
    lines = input.readlines()

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_names = {}

for x, n in enumerate(numbers):
    number_names[n] = x + 1

result = 0

def find_numeric(string, reverse = False):

    global numbers
    global number_names

    if not reverse:

        for x, symbol in enumerate(string):
            if symbol.isnumeric():
                return int(symbol)
                
            elif symbol.isalpha():
                for n in numbers:
                    if symbol == n[0]:
                        if line.find(n) == x:
                            return number_names[n]
    
    else:
        string = string[::-1]
        
        for x, symbol in enumerate(string):
            if symbol.isnumeric():
                return int(symbol)
                
            elif symbol.isalpha():
                for n in numbers:
                    if symbol == n[-1]:
                        if string.find(n[::-1]) == x:
                            return number_names[n]

    return None

for line in lines:
    line_val = 10 * find_numeric(line) + find_numeric(line, reverse = True)
    result += line_val
    
print(result)