with open("AoC_7_input.txt") as f:
    crab_positions = f.readline().split(",")
crab_positions = [int(x) for x in crab_positions]
print(crab_positions)
print(type(crab_positions))

possible_positions = range(max(crab_positions))

min_fuel_usage = None
min_fuel_usage_target_position = None
for target_position in possible_positions:
    current_fuel_use = 0
    for crab_position in crab_positions:
        current_fuel_use += abs(crab_position-target_position)
    if min_fuel_usage == None or current_fuel_use < min_fuel_usage:
        min_fuel_usage = current_fuel_use
        min_fuel_usage_target_position = target_position


print(min_fuel_usage)

