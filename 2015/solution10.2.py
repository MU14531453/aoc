
with open('input10.txt', 'r') as input:
    
    text = input.read()


def say(text, iterations_left = 39):
    
    result = []

    text = list(text) + ['q']
    base = text[0]

    for x, val in enumerate(text):

        if text[x+1] == base[0]:
            base = base + val
        elif text[x + 1] == 'q':
            result.append(base)
            break
        else:
            result.append(base)
            base = text[x+1]

    for x, string in enumerate(result):
        result[x] = str(len(string)) + str(string[0])\
        
    result = ''.join(result)
    

    if iterations_left == 0:
        return result
    else:
        return say(result, iterations_left = iterations_left - 1)
    
print(len(say(text = text, iterations_left = 49)))
