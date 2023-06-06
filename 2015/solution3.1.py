with open('input3.txt', 'r') as input:

    coords = set()
    coords.add((0,0))

    directions = input.read()
    current_state = [0,0]

    for arrow in directions:
        if arrow == '^':
            current_state = current_state[0] + 1, current_state[1]
            coords.add(tuple(current_state))
        elif arrow == 'v':
            current_state = current_state[0] - 1, current_state[1]
            coords.add(tuple(current_state))
        elif arrow == '<':
            current_state = current_state[0], current_state[1] - 1
            coords.add(tuple(current_state))
        elif arrow == '>':
            current_state = current_state[0], current_state[1] + 1
            coords.add(tuple(current_state))

    print(len(coords))