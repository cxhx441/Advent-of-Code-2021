with open("AoC_11_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]

octopus = []
for line in lines:
    temp = list()
    for ch in line:
        temp.append(int(ch))
    octopus.append(temp)

def is_top(row):
    return row == 0
def is_right(column):
    return column == len(octopus[0]) - 1
def is_bottom(row):
    return row == len(octopus) -1
def is_left(column):
    return column == 0
def is_top_left(row, column):
    return is_top(row) and is_left(column)
def is_top_right(row, column):
    return is_top(row) and is_right(column)
def is_bottom_right(row, column):
    return is_bottom(row) and is_right(column)
def is_bottom_left(row, column):
    return is_bottom(row) and is_left(column)

def increment_all_octopus():
    for row in range(len(octopus)):
        for column in range(len(octopus[row])):
            octopus[row][column] += 1

def flash_octopus(flashed_this_step):
    for row in range(len(octopus)):
        for column in range(len(octopus[row])):
            if octopus[row][column] > 9 and (row, column) not in flashed_this_step:
                flashed_this_step.add((row, column))
                increment_adjacent(row, column)
                flash_adjacent(row, column, flashed_this_step)

def flash_adjacent(row, column, flashed_this_step):
    #top
    if not is_top(row):
        this_row = row-1
        this_column = column
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #topright
    if not is_top(row) and not is_right(column):
        this_row = row-1
        this_column = column+1
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #right
    if not is_right(column):
        this_row = row
        this_column = column+1
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #bottomright
    if not is_bottom(row) and not is_right(column):
        this_row = row+1
        this_column = column+1
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #bottom
    if not is_bottom(row):
        this_row = row+1
        this_column = column
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #bottomleft
    if not is_bottom(row) and not is_left(column):
        this_row = row+1
        this_column = column-1
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #left
    if not is_left(column):
        this_row = row
        this_column = column-1
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)
    #topleft
    if not is_top(row) and not is_left(column):
        this_row = row-1
        this_column = column-1
        if octopus[this_row][this_column] > 9 and (this_row, this_column) not in flashed_this_step:
            flashed_this_step.add((this_row, this_column))
            increment_adjacent(this_row, this_column)
            flash_adjacent(this_row, this_column, flashed_this_step)


def increment_adjacent(row, column):
    #top
    if not is_top(row):
        octopus[row-1][column] += 1
    #topright
    if not is_top(row) and not is_right(column):
        octopus[row-1][column+1] += 1
    #right
    if not is_right(column):
        octopus[row][column+1] += 1
    #bottomright
    if not is_bottom(row) and not is_right(column):
        octopus[row+1][column+1] += 1
    #bottom
    if not is_bottom(row):
        octopus[row+1][column] += 1
    #bottomleft
    if not is_bottom(row) and not is_left(column):
        octopus[row+1][column-1] += 1
    #left
    if not is_left(column):
        octopus[row][column-1] += 1
    #topleft
    if not is_top(row) and not is_left(column):
        octopus[row-1][column-1] += 1

def set_flashed_to_zero():
    for row in range(len(octopus)):
        for column in range(len(octopus[row])):
            if octopus[row][column] > 9:
                octopus[row][column] = 0

def count_greater_than_9():
    count = 0
    for row in octopus:
        for num in row:
            if num > 9:
                count +=1
    return count

def increment_step(num_steps):
    flash_count = 0
    for cur_step_num in range(num_steps):
        # step 1: increase each octopus by 1
        increment_all_octopus()
        # step 2: flash any octopus with energy > 9 and not already flashed
            # note any flashers
            # increase adjacent (including diagonal) octopus by 1
                # flash if > 9, increase adjacent and not already flashed
        flashed_this_step = set()
        flash_octopus(flashed_this_step)
        flash_count += count_greater_than_9()
        set_flashed_to_zero()
        if len(flashed_this_step) == len(octopus[0]) * len(octopus):
            print(f'WE DID IT IN {cur_step_num+1} steps!')
            break
    return flash_count
# for line in octopus:
#     print(line)
# print()
flash_count = increment_step(2000)
# for line in octopus:
#     print(line)
# print(f'flashcount {flash_count}')

# step2_check = '8807476555 5089087054 8597889608 8485769600 8700908800 6600088989 6800005943 0000007456 9000000876 8700006848'
# step1_check ='6594254334 3856965822 6375667284 7252447257 7468496589 5278635756 3287952832 7993992245 5957959665 6394862637'
# step3_check = '0050900866 8500800575 9900000039 9700000041 9935080063 7712300000 7911250009 2211130000 0421125000 0021119000'
# step4_check = '2263031977 0923031697 0032221150 0041111163 0076191174 0053411122 0042361120 5532241122 1532247211 1132230211'
# step100_check = '0397666866 0749766918 0053976933 0004297822 0004229892 0053222877 0532222966 9322228966 7922286866 6789998766'
# step02_check = '45654 51115 61116 51115 45654'
# step_check = step100_check
# # step2_check = '45654 51115 61116 51115 45654'
# step_check = step_check.split(" ")
# new_list = []
# for string in step_check:
#     new_list.append([int(x) for x in string])
# step_check = new_list

# print(step_check == octopus)

# error_key = list()
# for row in range(len(octopus)):
#     error_key_row = list()
#     for column in range(len(octopus[row])):
#         if octopus[row][column] == step_check[row][column]:
#             error_key_row.append('.|.')
#         else:
#             error_key_row.append(f'{octopus[row][column]}|{step_check[row][column]}')
#     error_key.append(error_key_row)

# for row in error_key:
#     print(row)
