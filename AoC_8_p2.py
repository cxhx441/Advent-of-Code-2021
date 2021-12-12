#TODO Refactor that algo for getting the digits/segments to including filtering based on the number of times the segments occurs (which is different depending on the segment)
with open("AoC_8_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]
outputs = [0]*len(lines)
inputs = [0]*len(lines)
for i in range(len(lines)):
    outputs[i] = lines[i].split(" | ")[1].split(" ")
    inputs[i] = lines[i].split(" | ")[0].split(" ")
for output in outputs:
    for idx in range(len(output)):
        output[idx] = set(output[idx])
for input_val in inputs:
    for idx in range(len(input_val)):
        input_val[idx] = set(input_val[idx])
print(input_val)
def solve_for_this_one(input_list, output):
    digits = dict()
    for idx in range(10):
        digits[idx] = None
    segments = dict()
    for input_set in input_list:
        # 1 = sets of 2
        if len(input_set) == 2:
            digits[1] = input_set
        # 4 = sets of 4
        elif len(input_set) == 4:
            digits[4] = input_set
        # 7 = sets of 3
        elif len(input_set) == 3:
            digits[7] = input_set
        # 8 = sets of 7
        elif len(input_set) == 7:
            digits[8] = input_set

    # a segment = 7set - 1set
    segments['a'] = digits[7] - digits[1]
    # c segment = 1set - set_of_6 that has 1 segment left
    sets_of_6 = [x for x in input_list if len(x) == 6]
    segments['c'] = digits[1] - [x for x in sets_of_6 if len(digits[1]-x) == 1][0]
    # 6 = 8set - cseg
    digits[6] = digits[8] - segments['c']
    # 5 = set_of_5 - 6set that has 0 segments left
    sets_of_5 = [x for x in input_list if len(x) == 5]
    digits[5] = [x for x in sets_of_5 if len(x-digits[6]) == 0][0]
    # e segment = 8set - 5set -cseg
    segments['e'] = digits[8] - digits[5] - segments['c']
    # g segment = 8set - 4set - a_seg - e seg
    segments['g'] = digits[8] - digits[4] - segments['a'] - segments['e']
    # d segment = OF SETS OF 5 - ASEG - GSEG4set - 1set - bseg
    cur_set = set()
    for set_of_5 in sets_of_5:
        for ch in set_of_5:
            if ch in sets_of_5[0] and ch in sets_of_5[1] and ch in sets_of_5[2]:
                cur_set.add(ch)
    segments['d'] = cur_set - segments['a'] - segments['g']
    # b segment = 4set - 1set - dseg
    segments['b'] = digits[4] - digits[1] - segments['d']
    # f segment =  8set - aseg - bseg - cseg - dseg - eseg - gseg
    segments['f'] = digits[8] - segments['a'] - segments['b'] - segments['c'] - segments['d'] - segments['e'] - segments['g']


    # 0 = 8set - dseg
    digits[0] = digits[8] - segments['d']
    # 2 = 8set - bseg - fseg
    digits[2] = digits[8] - segments['b'] - segments['f']
    # 3 = 8set - bseg - eseg
    digits[3] = digits[8] - segments['b'] - segments['e']
    # 9 = 8seg - eseg
    digits[9] = digits[8] - segments['e']

    # #flip digits and keys
    # new_digits = dict()
    # for key in digits:
    #     print(digits[key])
    #     new_digits[digits[key]] = key

    #calculate total for this output
    print("xxx")
    digits_list = list(digits.values())
    cur_num_str = ''
    for output_set in output:
        cur_num_str += str(digits_list.index(output_set))
    return int(cur_num_str)

total = 0
for idx in range(len(inputs)):
    total += solve_for_this_one(inputs[idx], outputs[idx])

print(total)
