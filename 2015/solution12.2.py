with open('input12.txt.', 'r') as input:

    text = input.read()

red = 'red'

item_starts = [x for x, char in enumerate(text) if char == "{"]
item_stops = [x for x, char in enumerate(text) if char == "}"]
bracket_starts = [x for x, char in enumerate(text) if char == "["]
bracket_stops = [x for x, char in enumerate(text) if char == "]"]

filtered_text = text[:item_starts[0]]

for x, start in enumerate(item_starts):
    stop = item_stops[x]
    if red in text[start:stop]:
        if any([red in text[bracket_starts[x]:bracket_stops[x]] for x, _ in enumerate(bracket_starts) if _ in range(start,stop)]):
            filtered_text += text[start:stop]
        else:
            filtered_text += ":" * (bracket_stops[x] - bracket_starts[x])
    else:
        filtered_text += text[start:stop]
    filtered_text += text[stop:item_starts[x+1]]


text = text.replace('[', "'").replace(']', "'").replace('{', "'").replace('}', "'").replace(':', "'").replace(',', "'").split("'")

result = 0

for entry in text:
    try:
        result += int(entry)
    except ValueError:
        pass



print(result)

#  > 93127