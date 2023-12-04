
with open('input4.txt', 'r') as input:

    lines = input.readlines()

result = 0

for line in lines:
    line = line.split(':')[1]
    
    winning_numbers, drawn_numbers = [int(i) for i in line.split('|')[0].split(' ') if i], [int(i) for i in line.split('|')[1].split(' ') if i]
    power = sum([drawn_numbers.count(n) for n in winning_numbers]) - 1
    
    if power < 0:
        pass
    else:
        result += 2 ** power

print(result)