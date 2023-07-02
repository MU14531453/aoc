with open('input20.txt', 'r') as input:

    value = int(int(input.read()) / 10)

lower_bound = 720720

# Taken from the highly composite number list
# https://oeis.org/A002182

if lower_bound % 2:
    lower_bound += 1

current = lower_bound

while True:

    result = current
    for divisor in range(1, current // 2 + 2):
        if not current % divisor:
            result += divisor
    if result > value:
        print(current)
        break
    else:
        current += 210
        # the bigger first prime product in increment the faster result, but it can overkill
    