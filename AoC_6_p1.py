with open("AoC_6_input_sample.txt") as f:
    lantern_fish = f.readline().split(",")
lantern_fish = [int(x) for x in lantern_fish]

for i in range(80):
    zero_count = lantern_fish.count(0)
    lantern_fish = [x-1 for x in lantern_fish]
    for _ in range(zero_count):
        lantern_fish.append(8)
    lantern_fish = [6 if x == -1 else x for x in lantern_fish]

print(len(lantern_fish))



