with open("AoC_3_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]
# print(lines)

ox_bits_list = lines
co2_bits_list = lines
def find_the_one(listy, criteria="max"):
    for bit_pos in range(12):
        count = 0
        if len(listy)>1:
            for bin_num in listy:
                if bin_num[bit_pos] == "1":
                    count += 1
                else:
                    count -= 1

            if count >= 0:
                if criteria == "max":
                    listy = [x for x in listy if x[bit_pos] == '1']
                if criteria == "min":
                    listy = [x for x in listy if x[bit_pos] == '0']
            else:
                if criteria == "max":
                    listy = [x for x in listy if x[bit_pos] == '0']
                if criteria == "min":
                    listy = [x for x in listy if x[bit_pos] == '1']
    return listy

ox_bits_list = find_the_one(ox_bits_list, criteria="max")
co2_bits_list = find_the_one(co2_bits_list, criteria="min")

print(ox_bits_list)
print(co2_bits_list)

def real_bin_2_dec(binary):
    binary = int(binary)
    decimal, n = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal += dec * 2**n
        binary = binary//10
        n += 1
    return decimal

ox_dec = real_bin_2_dec(ox_bits_list[0])
co2_dec = real_bin_2_dec(co2_bits_list[0])
print(ox_dec)
print(co2_dec)
print(ox_dec*co2_dec)
