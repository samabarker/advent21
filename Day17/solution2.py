target_x_max = 227
target_x_min = 175
target_y_max = -79
target_y_min = -134

start_point = [0,0]
max_iters = 1000

def traj_check(initial_velocity, start_point):
    global target_x_max, target_x_min, target_y_max, target_y_min, max_iters
    for i in range(0,max_iters):
        if start_point[0] <= target_x_max and start_point[0] >= target_x_min and start_point[1] <= target_y_max and start_point[1] >= target_y_min:
            return True
        start_point = [start_point[0] + initial_velocity[0], start_point[1] + initial_velocity[1]]
        new_v_x = 0
        if initial_velocity[0] > 0:
            new_v_x = initial_velocity[0] - 1
        elif initial_velocity[0] < 0:
            new_v_x = initial_velocity[0] + 1
        initial_velocity = [new_v_x, initial_velocity[1]-1]
    return(False)


values = []
for x in range(0,228):
    for y in range(-135,135):
        if traj_check([x,y], start_point):
            values.append([x,y])

print(len(values))