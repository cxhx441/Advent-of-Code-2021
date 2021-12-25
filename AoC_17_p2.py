
# target area: x=48..70, y=-189..-148

positions_list = []
cur_position = [0, 0]
init_velocities_list = []
STARTING_Y_VELOCITY = 49
BEST_STARTING_X = None
velocity = [0, STARTING_Y_VELOCITY]
velocities_list = []
hit_velocities = []

target_x = range(48, 70+1)
target_y = range(-189, -148 + 1)

def is_in_target():
    return (cur_position[0] in target_x) and (cur_position[1] in target_y)

def step():
    cur_position[0] += velocity[0]
    cur_position[1] += velocity[1]

    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1

    velocity[1] -= 1

    # positions_list.append(tuple(cur_position))

def is_past_target():
    return cur_position[0] > 70 or cur_position[1] < -189

def try_velocity():
    init_velocities_list.append(velocity.copy())
    BEST_STARTING_X = None
    while not is_past_target():
        positions_list.append(cur_position.copy())
        velocities_list.append(velocity.copy())
        step()
        if is_in_target():
            print("\nin target")
            positions_list.append(cur_position.copy())
            velocities_list.append(velocity.copy())

            # print(init_velocities_list[-1])
            # print(positions_list)
            BEST_STARTING_X = init_velocities_list[-1][0]
            cur_position_list = positions_list.copy()
            while len(positions_list) > 0:
                positions_list.pop()
            while len(velocities_list) > 0:
                velocities_list.pop()
            cur_position[0], cur_position[1] = 0, 0
            last_velocity = init_velocities_list[-1]
            velocity[0] = BEST_STARTING_X
            velocity[1] = last_velocity[1]+1
            init_velocities_list.append(velocity.copy())
            # return
            if BEST_STARTING_X != None:
                print("final in target")
                print(init_velocities_list[-1])
                print(cur_position_list)
                return ("in target", cur_position_list)
        # if not moving right and too far left
        if velocity[0] == 0 and cur_position[0] < target_x[0] and BEST_STARTING_X == None:
            # print("\nIncrease X Velocity")
            while len(positions_list) > 0:
                positions_list.pop()
            while len(velocities_list) > 0:
                velocities_list.pop()
            cur_position[0], cur_position[1] = 0, 0
            last_velocity = init_velocities_list[-1]
            velocity[0] = last_velocity[0]+1
            velocity[1] = STARTING_Y_VELOCITY
            init_velocities_list.append(velocity.copy())
        # elif BEST_STARTING_X != None:
        #     print(init_velocities_list[-1])
        #     return
    # print("\npast target")
    # print(positions_list)
    # print(init_velocities_list)
    # print(init_velocities_list[-1])
    # print(positions_list)
    return "past target"

# try_velocity()



# for num in range(49, 200):
#     print("retry")
#     positions_list = []
#     cur_position = [0, 0]
#     init_velocities_list = []
#     STARTING_Y_VELOCITY = num
#     BEST_STARTING_X = None
#     velocity = [0, STARTING_Y_VELOCITY]
#     velocities_list = []
#     returned_tuple = try_velocity()
#     if type(returned_tuple) == tuple:
#         print(returned_tuple[0])
#         cur_max = 0
#         for pos in returned_tuple[1]:
#             if pos[1] > cur_max:
#                 cur_max = pos[1]
#         print(cur_max)

for x in range(0, 200):
    for y in range(-300, 300):
        cur_position[0], cur_position[1] = 0, 0
        velocity = [x, y]
        init_velocities_list.append(velocity.copy())
        while not is_past_target() or is_in_target():
            step()
            if is_in_target():
                hit_velocities.append(init_velocities_list[-1].copy())
                print("hit")
                break
        print("miss")
        cur_position[0], cur_position[1] = 0, 0
print(hit_velocities)
print(len(hit_velocities))
