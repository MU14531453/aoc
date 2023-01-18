with open(r'input1.txt', 'r') as input:
    string = input.read()
    result = string.count('(') - string.count(')')
    print(result)