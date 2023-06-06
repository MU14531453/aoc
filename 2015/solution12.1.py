with open('input12.txt.', 'r') as input:

    text = input.read()

text = text.replace('[', "'").replace(']', "'").replace('{', "'").replace('}', "'").replace(':', "'").replace(',', "'").split("'")

result = 0

for entry in text:
    try:
        result += int(entry)
    except ValueError:
        pass

print(result)