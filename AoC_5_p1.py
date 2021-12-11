with open("AoC_5_input.txt") as f: 
    lines = f.readlines()

# lines = [x[:-1] for x in lines]
lines = [x.replace(' -> ', ',') for x in lines]
lines = [x.split(",") for x in lines]
#get in the format [[x1, y1, x2, y2], ...]
for idx in range(len(lines)):
    for jdx in range(len(lines[idx])):
        lines[idx][jdx] = int(lines[idx][jdx])

# print(lines)
# remove vents where x1 != x2 and y1 !=y2
for line in lines:
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if x1 != x2 and y1 != y2:
        lines.remove(line)

vent_coordinates = lines

# creating blank grid
grid = []
max_x = 0
max_y = 0
#max_x = max of x1 and x2s
#max_y = max of y1 and y2s
for vent_coord in vent_coordinates: 
    x1, y1, x2, y2 = vent_coord[0], vent_coord[1], vent_coord[2], vent_coord[3]
    max_x = max(x1, x2, max_x) 
    max_y = max(y1, y2, max_y) 
row = ['.' for x in range(max_x+1)] 
for idx in range(max_y+1):
    grid.append(list(row))
# print(grid)
# print(len(grid))
# print(len(grid[0]))

def grid_markup(grid, coord_range, static_coord, mover):
    # print(f"mover: {mover}")
    if mover == "x":
        for x_coord in coord_range:
            # print(f"static_coord {static_coord}")
            # print(f"x_coord {x_coord}")
            if grid[static_coord][x_coord] == '.':
                grid[static_coord][x_coord] = 1
            else:
                grid[static_coord][x_coord] += 1

    elif mover == "y":
        for y_coord in coord_range:
            if grid[y_coord][static_coord] == '.':
                grid[y_coord][static_coord] = 1
            else:
                grid[y_coord][static_coord] += 1
    # for el in grid:
    #     print(el)


# for el in grid:
#     print(el)
#fill grid
for vent_coord in vent_coordinates:
    x1, y1, x2, y2 = vent_coord[0], vent_coord[1], vent_coord[2], vent_coord[3]
    # print(x1, y1, x2, y2)
    if y1 == y2: 
        grid_markup(grid, range(min(x1,x2), max(x1, x2)+1), y1, "x")
    elif x1 == x2: 
        grid_markup(grid, range(min(y1, y2), max(y1, y2)+1), x1, "y")



#count the 
count = 0
for lst in grid:
    for el in lst:
        if el != '.' and el > 1:
            count+=1

print(count) 