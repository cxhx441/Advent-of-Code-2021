with open("AoC_14_input_sample.txt") as f:
    lines = f.read()

lines = lines.split('\n\n')
poly_template = lines[0]
pair_insert_string = lines[1].split('\n')
pair_insert = dict()
for string in pair_insert_string[:-1]:
    pair_insert[string[:2]] = string[-1]

def update_count(string, dict_count, count_up_down='up'):
    if string in dict_count.keys():
        if count_up_down == 'down':
            dict_count[string] -= 1
        else:
            dict_count[string] += 1
    else:
        dict_count[string] = 1
    return dict_count

char_count = dict()
for char in poly_template:
    char_count = update_count(char, char_count)

pair_count = pair_insert.copy()
for key in pair_count:
    pair_count[key] = 0
for idx in range(len(poly_template)-1):
    cur_pair = poly_template[idx] + poly_template[idx+1]
    pair_count = update_count(cur_pair, pair_count)

#update
def run_insert(pair_count, char_count):
    temp_pair_count = pair_count.copy()
    for key in pair_count:
        if temp_pair_count[key] > 0:
            for char_insert in pair_insert[key]:
                char_count = update_count(char_insert, char_count)
                temp_pair_count = update_count(key, pair_count, count_up_down='down')
                temp_pair_count = update_count(key[0]+char_insert, temp_pair_count)
                temp_pair_count = update_count(char_insert+key[1], temp_pair_count)
    return (temp_pair_count, char_count)


print(poly_template)
print(pair_insert)
print(char_count)
print(pair_count)

pair_count, char_count = run_insert(pair_count, char_count)

print(poly_template)
print(pair_insert)
print(char_count)
print(pair_count)

