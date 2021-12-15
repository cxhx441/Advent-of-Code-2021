with open("AoC_14_input.txt") as f:
    lines = f.read()

lines = lines.split('\n\n')
poly_template = lines[0]
pair_insert_string = lines[1].split('\n')
pair_insert = dict()
for string in pair_insert_string[:-1]:
    pair_insert[string[:2]] = string[-1]

def update_count(string, dict_count, num, count_up_down='up'):
    if string in dict_count:
        if count_up_down == 'down':
            dict_count[string] -= num
        else:
            dict_count[string] += num
    else:
        dict_count[string] = 1
    return dict_count

char_count = dict()
for char in poly_template:
    char_count = update_count(char, char_count, 1)

pair_count = pair_insert.copy()
for key in pair_count:
    pair_count[key] = 0
for idx in range(len(poly_template)-1):
    cur_pair = poly_template[idx] + poly_template[idx+1]
    pair_count = update_count(cur_pair, pair_count, 1)

#update
def run_insert(pair_count, char_count):
    pairs_to_add = pair_count.copy()
    pairs_to_remove = pair_count.copy()
    for key in pair_count:
        pairs_to_add[key] = 0
        pairs_to_remove[key] = 0
    for pair in pair_count:
        # for _ in range(pair_count[pair]):
        #     char_insert = pair_insert[pair]
        #     char_count = update_count(char_insert, char_count, 1)
        #     pairs_to_add = update_count(pair[0]+char_insert, pairs_to_add, 1)
        #     pairs_to_add = update_count(char_insert+pair[1], pairs_to_add, 1)
        #     pairs_to_remove = update_count(pair, pairs_to_remove, 1)
        num_count = pair_count[pair]
        char_insert = pair_insert[pair]
        char_count = update_count(char_insert, char_count, num_count)
        pairs_to_add = update_count(pair[0]+char_insert, pairs_to_add, num_count)
        pairs_to_add = update_count(char_insert+pair[1], pairs_to_add, num_count)
        pairs_to_remove = update_count(pair, pairs_to_remove, num_count)
    for pair in pair_count:
        pair_count[pair] += pairs_to_add[pair]
        pair_count[pair] -= pairs_to_remove[pair]
    return (pair_count, char_count)


print(poly_template)
print(pair_insert)
print(char_count)
print(pair_count)

for _ in range(40):
    pair_count, char_count = run_insert(pair_count, char_count)

total = 0
for char in char_count:
    total += char_count[char]
print(total)
min_char = None
max_char = None
for char in char_count:
    if min_char == None or min_char > char_count[char]:
        min_char = char_count[char]
    if max_char == None or max_char < char_count[char]:
        max_char = char_count[char]
print(max_char)
print(min_char)
print(max_char - min_char)


# print(poly_template)
# print(pair_insert)
print(char_count)
print(pair_count)
print(char_count)

