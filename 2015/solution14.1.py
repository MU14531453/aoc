
def get_distance(speed, move_time, rest_time, endpoint):

    current_time = 0
    distance_travelled = 0

    moving = True

    while current_time < endpoint:
        if moving:
            for second in range(move_time):
                current_time += 1
                distance_travelled += speed

                if current_time == endpoint:
                    return distance_travelled
                
            moving = False
        
        else:
            current_time += rest_time

            if current_time >= endpoint:
                return distance_travelled
            
            moving = True

    return None


with open('input14.txt.', 'r') as input:

    text = input.readlines()


finish_time = 2503

result = []

for line in text:

    line_vals = line.split(' ')

    reindeer_parameters = []

    for word in line_vals:
        try:
            reindeer_parameters.append(int(word))
        except ValueError:
            pass

    result.append(get_distance(speed = reindeer_parameters[0],
                                move_time = reindeer_parameters[1],
                                rest_time = reindeer_parameters[2],
                                endpoint = finish_time))
    
print(max(result))
