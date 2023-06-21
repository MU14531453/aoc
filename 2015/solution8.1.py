import os
os.chdir(r'c:\Users\uz\aoc\2015')

with open('input8.txt', 'rb') as input:
    
    text = input.readlines()

    

text = ['""', '"abc"', '"aaa\"aaa"', '"\x27"']



result = 0

for line in text:
    print(line)
    
# print(result)
# < 1379
# > 1079