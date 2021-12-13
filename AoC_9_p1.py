with open("AoC_9_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]

heightmap = []
for line in lines:
    cur_row = list()
    for char in line:
        cur_row.append(int(char))
    heightmap.append(cur_row)
del cur_row
del line
del char
del lines

def is_top(row):
    return row == 0

def is_right(heightmap, column):
    return column == len(heightmap[0]) - 1

def is_bottom(heightmap, row):
    return row == len(heightmap) -1

def is_left(column):
    return column == 0

def is_top_left(row, column):
    return is_top(row) and is_left(column)

def is_top_right(heightmap, row, column):
    return is_top(row) and is_right(heightmap, column)

def is_bottom_right(heightmap, row, column):
    return is_bottom(heightmap, row) and is_right(heightmap, column)

def is_bottom_left(heightmap, row, column):
    return is_bottom(heightmap, row) and is_left(column)

def compare(heightmap, row, column, direction):
    flag = True
    if 'up' in direction and flag == True:
        flag = heightmap[row][column] < heightmap[row-1][column]
    if 'right' in direction and flag == True:
        flag = heightmap[row][column] < heightmap[row][column+1]
    if 'down' in direction and flag == True:
        flag = heightmap[row][column] < heightmap[row+1][column]
    if 'left' in direction and flag == True:
        flag = heightmap[row][column] < heightmap[row][column-1]
    return flag

def is_lowest(heightmap, row, column) -> bool:
    if is_top_left(row, column):
        direction = ('down', 'right')
        return compare(heightmap, row, column, direction)
    elif is_top_right(heightmap, row, column):
        #compare down, left
        direction = ('down', 'left')
        return compare(heightmap, row, column, direction)
    elif is_bottom_right(heightmap, row, column):
        #compare left, up
        direction = ('left', 'up')
        return compare(heightmap, row, column, direction)
    elif is_bottom_left(heightmap, row, column):
        #compare right, up
        direction = ('right', 'up')
        return compare(heightmap, row, column, direction)
    elif is_top(row):
        #compare left, right, down
        direction = ('left', 'right', 'down')
        return compare(heightmap, row, column, direction)
    elif is_right(heightmap, column):
        #compare up, down, left
        direction = ('up', 'down', 'left')
        return compare(heightmap, row, column, direction)
    elif is_bottom(heightmap, row):
        #compare left, right, up
        direction = ('left', 'right', 'up')
        return compare(heightmap, row, column, direction)
    elif is_left(column):
        #compare up, right, down
        direction = ('up', 'right', 'down')
        return compare(heightmap, row, column, direction)
    else:
        #compare up, down, left, right
        direction = ('up', 'down', 'left', 'right')
        return compare(heightmap, row, column, direction)

risk_level = 0
for row in range(len(heightmap)):
    for column in range(len(heightmap[row])):
        if is_lowest(heightmap, row, column):
            risk_level += heightmap[row][column] + 1

print(risk_level)
