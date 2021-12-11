with open('AoC_1_input.txt', 'r') as f:
    lines = f.readlines()

for idx in range(len(lines)):
    line = lines[idx]
    lines[idx] = int(line)
print(lines)

sum_of_threes = []

for idx in range(2, len(lines)):
    sum = lines[idx-2] + lines[idx-1] + lines[idx]
    sum_of_threes.append(sum)
print(sum_of_threes)
def count_when_next_idx_is_greater(input_list):
    count = 0
    for idx in range(1, len(input_list)):
        if input_list[idx] > input_list[idx-1]:
            count += 1
            # print(f'{input_list[idx]} > {input_list[idx-1]}: True!')
    print(count)

count_when_next_idx_is_greater(lines)
count_when_next_idx_is_greater(sum_of_threes)

