with open('input2.txt', 'r') as input:

    result = 0

    for line in input.readlines():
        size = line.split('x')
        size = [int(i) for i in size]
        result += (size[0] * size[1] * size[2])
        size.remove(max(size))
        result += 2 * (size[0] + size[1])

    print(result)