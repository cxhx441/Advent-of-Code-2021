with open("AoC_8_input.txt") as f:
    lines = f.readlines()
lines = [x[:-1] for x in lines]
outputs = [0]*len(lines)
for i in range(len(lines)):
    outputs[i] = lines[i].split(" | ")[1].split(" ")

count = 0
for output in outputs:
    for el in output:
        if len(el) in (2, 4, 3, 7):
            count += 1

print(count)
