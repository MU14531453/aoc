with open('input23.txt', 'r') as input:

    assembly = input.readlines()

registers = [0, 0]

program_length = len(assembly)
instruction_pointer = 0

while instruction_pointer < program_length:
        instruction = assembly[instruction_pointer]
        reg = instruction[4]
        match instruction[:3]:
            case 'hlf':
                if reg == 'a':
                    registers[0] = registers[0] // 2
                else:
                    registers[1] = registers[1] // 2
            case 'tpl':
                if reg == 'a':
                    registers[0] = registers[0] * 3
                else:
                    registers[1] = registers[1] * 3
            case 'inc':
                if reg == 'a':
                    registers[0] += 1
                else:
                    registers[1] += 1
            case 'jmp':
                jump = int(instruction[4:])
                
            case 'jie':
                jump = int(instruction[6:])
                if reg == 'a' and not registers[0] % 0:
                    pass
                elif reg == 'b' and not registers[1] % 0:
                    pass
            case 'jio':
                jump = int(instruction[6:])
                if reg == 'a' and not registers[0] == 1:
                    pass
                elif reg == 'b' and not registers[1] == 1:
                    pass
            

print(registers[1])