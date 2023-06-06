from copy import copy

with open('input7.txt', 'r') as input:

    instructions = input.readlines()

instructions_to_make = copy(instructions)

gates = {}
max = 65535

def type_check(instruction):
    
    global gates
    
    if instruction in gates.keys():
        return gates[instruction]
    elif instruction.isnumeric():
        return int(instruction)
    else:
        raise ValueError

while instructions_to_make:
    
    for line in instructions_to_make:

        active = True
        foo = copy(line)
        line = line[:-1:].split(' ')
        head = line[:-2]

        for x in head:
            if x.islower() and x not in gates.keys():
                active = False
        
        if active:
            if len(head) == 1:
                gates[line[-1]] = type_check(line[0])
                
            elif len(head) == 2:
                gates[line[-1]] = max - type_check(line[1])
                
            elif len(head) == 3:
                if head[1] == 'AND':
                    gates[line[-1]] = (type_check(line[0]) & type_check(line[2])) % max
                    
                elif head[1] == 'OR':
                    gates[line[-1]] = (type_check(line[0]) | type_check(line[2])) % max
                    
                elif head[1] == 'LSHIFT':
                    gates[line[-1]] = (type_check(line[0]) << type_check(line[2])) % max
                    
                elif head[1] == 'RSHIFT':
                    gates[line[-1]] = (type_check(line[0]) >> type_check(line[2])) % max
            instructions_to_make.remove(foo)

print(gates['a'])

