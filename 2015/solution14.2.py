
import numpy as np

def update_distance(speed, move_time, rest_time, endpoint):

    result = []
    distance = 0


    moving = True
    second = 0

    current_interval = move_time

    while second < endpoint:
                
        if moving:
            distance = distance + speed
            result.append(distance)
            current_interval -= 1
            if current_interval == 0:
                moving = False
                current_interval = rest_time
        
        else:
            result.append(distance)
            current_interval -= 1
            if current_interval == 0:
                moving = True
                current_interval = move_time

        second += 1

    return result


with open('input14.txt.', 'r') as input:

    text = input.readlines()


finish_time = 2503

positions = []

for line in text:

    line_vals = line.split(' ')

    reindeer_parameters = []

    for word in line_vals:
        try:
            reindeer_parameters.append(int(word))
        except ValueError:
            pass

    positions.append(update_distance(speed = reindeer_parameters[0],
                                move_time = reindeer_parameters[1],
                                rest_time = reindeer_parameters[2],
                                endpoint = finish_time))
    

points = [0 for _ in range(len(positions))]

positions = np.array(positions, dtype = np.int32)

for second in range(positions.shape[1]):
    for x, val in enumerate(positions[...,second]):
        if val == positions[...,second].max():
            points[x] += 1

print(max(points))
