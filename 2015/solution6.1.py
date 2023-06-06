import numpy as np

with open('input6.txt', 'r') as input:

    instructions = input.readlines()

lights = np.zeros((1000,1000), dtype = np.int8)

def parser(line):
    flag = None
    
    if 'toggle' in line:
        line = line[7:]
        line = line.split('through')
        line = [_.split(',') for _ in line]
        line = [[int(x) for x in coord] for coord in line]
        flag = 0
    elif 'turn off' in line:
        line = line[9:]
        line = line.split('through')
        line = [_.split(',') for _ in line]
        line = [[int(x) for x in coord] for coord in line]
        flag = 1
    elif 'turn on' in line:
        line = line[8:]
        line = line.split('through')
        line = [_.split(',') for _ in line]
        line = [[int(x) for x in coord] for coord in line]
        flag = 2
    
    return (line, flag)

for line in instructions:
    instruction = parser(line = line)
    if instruction[1] == 0:
        lights[instruction[0][0][0]:instruction[0][1][0]+1, instruction[0][0][1]:instruction[0][1][1]+1] = (lights[instruction[0][0][0]:instruction[0][1][0]+1, instruction[0][0][1]:instruction[0][1][1]+1] + 1) % 2
    elif instruction[1] == 1:
        lights[instruction[0][0][0]:instruction[0][1][0]+1, instruction[0][0][1]:instruction[0][1][1]+1] = 0
    elif instruction[1] == 2:
        lights[instruction[0][0][0]:instruction[0][1][0]+1, instruction[0][0][1]:instruction[0][1][1]+1] = 1
    
print(np.sum(lights))
