with open('input23.txt', 'r') as input:

    assembly = input.readlines()

registers = [0, 0]

program_length = len(assembly) - 1
instruction_pointer = 0


while instruction_pointer < program_length:
        
        instruction = assembly[instruction_pointer]
        reg = instruction[4]

        match instruction[:3]:
            case 'hlf':
                instruction_pointer += 1
                if reg == 'a':
                    registers[0] = registers[0] // 2
                else:
                    registers[1] = registers[1] // 2
            case 'tpl':
                instruction_pointer += 1
                if reg == 'a':
                    registers[0] = registers[0] * 3
                else:
                    registers[1] = registers[1] * 3
            case 'inc':
                instruction_pointer += 1
                if reg == 'a':
                    registers[0] += 1
                else:
                    registers[1] += 1
            case 'jmp':
                jump = int(instruction[4:])
                instruction_pointer += jump
            case 'jie':
                jump = int(instruction[6:])
                if reg == 'a' and not registers[0] % 2:
                    instruction_pointer += jump
                elif reg == 'b' and not registers[1] % 2:
                    instruction_pointer += jump
                else:
                    instruction_pointer += 1
            case 'jio':
                jump = int(instruction[6:])
                if reg == 'a' and registers[0] == 1:
                    instruction_pointer += jump
                elif reg == 'b' and registers[1] == 1:
                    instruction_pointer += jump
                else:
                    instruction_pointer += 1
        print(registers, instruction)
            

print(registers[1])