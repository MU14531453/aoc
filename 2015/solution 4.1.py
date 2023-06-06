import hashlib

with open('input4.txt', 'r') as input:
    start = input.read()
    
count = 0

while True:
    hash = (start + str(count)).encode()
    result = hashlib.md5(hash).hexdigest()

    if result[:5] == '00000':
        print(count)
        break
    else:
        count += 1