with open('input1.txt', 'r') as input:
    string = input.read()
    
    current_floor = 0
    for x, brace in enumerate(string):
        if brace == '(':
            current_floor += 1
        elif brace == ')':
            current_floor -= 1
            if current_floor == -1:
                print(x + 1)
                break