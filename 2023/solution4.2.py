
with open('input4.txt', 'r') as input:

    lines = input.readlines()

card_count = [1 for _ in range(len(lines))]

for x, line in enumerate(lines):
    
    line = line.split(':')[1]
    
    winning_numbers, drawn_numbers = [int(i) for i in line.split('|')[0].split(' ') if i], [int(i) for i in line.split('|')[1].split(' ') if i]

    next_cards = sum([drawn_numbers.count(n) for n in winning_numbers])

    for _ in range(card_count[x]):
        for c in range(1, next_cards + 1):
            card_count[x + c] += 1

print(sum(card_count))