with open("AoC_2_input.txt") as f:
    lines = f.read()
lines = lines.split("\n")
lines = lines[:-1]
print(lines)

aim = 0
horizontal = 0
vertical = 0
for line in lines:
    direction = line.split()[0]
    count = int(line.split()[1])
    if direction == "up":
        aim -= count
    elif direction == "down":
        aim += count
    else:
        horizontal += count
        vertical += aim*count
print(horizontal)
print(vertical)
print(aim)
print(horizontal*vertical)
