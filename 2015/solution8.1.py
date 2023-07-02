# with open('input8.txt', 'rb') as input:
    
#     text = input.readlines()



text = ['""', '"abc"', '"aaa\"aaa"', '"\x27"']

for line in text:
    print(len(line))

text = [l.encode('utf-8') for l in text]
print('gadsfgdsafdasdf')
for line in text:
    print(len(line))

result = 0


    
# print(result)
# < 1379
# > 1079