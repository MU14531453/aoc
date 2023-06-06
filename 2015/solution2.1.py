with open('input2.txt', 'r') as input:

    result = 0

    for line in input.readlines():
        size = line.split('x')
        size = [int(i) for i in size]
        result += 2 * (size[0] * size[1] + size[1] * size[2] + size[2] * size[0])
        result += min(size[0] * size[1], size[1] * size[2], size[2] * size[0])
    
    print(result)