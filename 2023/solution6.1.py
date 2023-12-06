with open('input6.txt', 'r') as input:

    lines = input.readlines()

times = [int(i) for i in lines[0].split(':')[1].split(' ') if i]
distances = [int(i) for i in lines[1].split(':')[1].split(' ') if i]

result = 1
current = 0

for y, d in enumerate(distances):
    t = times[y]
    for n in range(t):
        speed = -n*(n-t) - d
        
        if speed > 0:
            current += 1
    result *= current
    current = 0

print(result)