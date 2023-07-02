with open('input3.txt', 'r') as input:

    coords = set()
    coords.add((0,0))

    directions = input.read()
    current_state_first = [0,0]
    current_state_second = [0,0]

    for arrow in directions[0::2]:
        if arrow == '^':
            current_state_first = current_state_first[0] + 1, current_state_first[1]
            coords.add(tuple(current_state_first))
        elif arrow == 'v':
            current_state_first = current_state_first[0] - 1, current_state_first[1]
            coords.add(tuple(current_state_first))
        elif arrow == '<':
            current_state_first = current_state_first[0], current_state_first[1] - 1
            coords.add(tuple(current_state_first))
        elif arrow == '>':
            current_state_first = current_state_first[0], current_state_first[1] + 1
            coords.add(tuple(current_state_first))
    
    for arrow in directions[1::2]:
        if arrow == '^':
            current_state_second = current_state_second[0] + 1, current_state_second[1]
            coords.add(tuple(current_state_second))
        elif arrow == 'v':
            current_state_second = current_state_second[0] - 1, current_state_second[1]
            coords.add(tuple(current_state_second))
        elif arrow == '<':
            current_state_second = current_state_second[0], current_state_second[1] - 1
            coords.add(tuple(current_state_second))
        elif arrow == '>':
            current_state_second = current_state_second[0], current_state_second[1] + 1
            coords.add(tuple(current_state_second))

    print(len(coords))