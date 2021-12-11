with open("AoC_2_input.txt") as f:
    lines = f.read()
lines = lines.split("\n")
lines = lines[:-1]
print(lines)

vertical = 0
horizontal = 0
for line in lines:
    direction = line.split()[0]
    count = int(line.split()[1])
    if direction == "up":
        vertical -= count
    elif direction == "down":
        vertical += count
    else:
        horizontal += count
print(horizontal)
print(vertical)
print(horizontal*vertical)
