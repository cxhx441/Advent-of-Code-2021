with open("AoC_6_input.txt") as f:
    lantern_fish_list = f.readline().split(",")
lantern_fish_list = [int(x) for x in lantern_fish_list]

# count number of 0s, 1s, 2s, 3s, 4s, 5s, 6s, 7s, 8s
    # store in dict
lantern_fish_dict = {0 : lantern_fish_list.count(0),
                     1 : lantern_fish_list.count(1),
                     2 : lantern_fish_list.count(2),
                     3 : lantern_fish_list.count(3),
                     4 : lantern_fish_list.count(4),
                     5 : lantern_fish_list.count(5),
                     6 : lantern_fish_list.count(6),
                     7 : lantern_fish_list.count(7),
                     8 : lantern_fish_list.count(8)}

# each day
for i in range(256):
    # store zeros_count
    zero_count = lantern_fish_dict[0]
    # count of each jumps to the lower bucket
    lantern_fish_dict_temp = {0 : lantern_fish_dict[1],
                            1 : lantern_fish_dict[2],
                            2 : lantern_fish_dict[3],
                            3 : lantern_fish_dict[4],
                            4 : lantern_fish_dict[5],
                            5 : lantern_fish_dict[6],
                            6 : lantern_fish_dict[7],
                            7 : lantern_fish_dict[8],
                            8 : lantern_fish_dict[0]}
    lantern_fish_dict = lantern_fish_dict_temp
    # zeros_count gets added to # of 6s
    lantern_fish_dict[6] += zero_count

print(sum(lantern_fish_dict.values()))




