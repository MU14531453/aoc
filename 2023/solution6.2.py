from math import sqrt

with open('input6.txt', 'r') as input:

    lines = input.readlines()

time = int(''.join([i for i in lines[0].split(':')[1].split(' ') if i]))
distance = int(''.join([i for i in lines[1].split(':')[1].split(' ') if i]))

speed_zeros = 1/2
delta = sqrt(time**2-4*distance)/2
sz_plus = speed_zeros + delta
sz_minus = speed_zeros - delta

print(int(sz_plus-sz_minus))

# both 6.1 and 6.2 algorithms solve each problem (this is O(1) time, 6.1 is O(n))