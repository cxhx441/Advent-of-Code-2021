import collections
import math
from collections import deque
# dijkstra's algorithm
def dijkstra(risk_grid, start, end):
    risk_to_rowcol = dict()
    path_to_rowcol = dict()
    previous_node = dict()
    unvisited_nodes = []
    for row in range(len(risk_grid)):
        for col in range(len(risk_grid[0])):
            risk_to_rowcol[(row, col)] = math.inf
            path_to_rowcol[(row, col)] = []
            unvisited_nodes.append((row, col))
    path_to_rowcol[(0, 0)] = collections.deque(start)
    risk_to_rowcol[(0, 0)] = 0
    adjacency_template = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    s = []
    while end not in s:
        # get lowest_risk_node
        # get cur_risk
        lowest_risk_node = end # obv not
        cur_risk = math.inf

        for node in unvisited_nodes:
        # for node in risk_to_rowcol:
        #     if node in s:
        #         continue
            if risk_to_rowcol[node] < risk_to_rowcol[lowest_risk_node]:
                lowest_risk_node = node
                cur_risk = risk_to_rowcol[node]
        # get adjacent_nodes (if node not in S)
        adjacent_nodes = []
        for adj_temp in adjacency_template:
            row = lowest_risk_node[0] + adj_temp[0]
            col = lowest_risk_node[1] + adj_temp[1]
            if (row, col) not in s and row >= 0 and row < len(risk_grid) and col >= 0 and col < len(risk_grid[0]):
                adjacent_nodes.append((row, col))

        # update each adjacent node
        for adj in adjacent_nodes:
            # risk = cur_risk + risk of the adjacent node
            risk = cur_risk + risk_grid[adj[0]][adj[1]]
            # if that risk is less than the current one, update it
            if risk < risk_to_rowcol[adj]:
                risk_to_rowcol[adj] = risk
                # cur_path = path_to_rowcol[lowest_risk_node].copy()
                # cur_path.append(adj)
                # path_to_rowcol[adj] = cur_path
                previous_node[adj] = lowest_risk_node
        unvisited_nodes.remove(lowest_risk_node)
        s.append(lowest_risk_node)
        print(lowest_risk_node)

    shortest_path = []
    node = end
    while node != start:
        shortest_path.append(node)
        node = previous_node[node]
    shortest_path.append(start)
    # shortest_path = path_to_rowcol[end]
    shortest_path.reverse()
    return shortest_path

# get input as grid
grid = []
with open("AoC_15_input.txt") as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
risk_grid = []
for row in lines:
    temp_row = list()
    for num in row:
        temp_row.append(int(num))
    risk_grid.append(temp_row.copy())

extend_amount = 5
new_risk_grid = []
for row in range(len(risk_grid)):
    new_risk_grid.append([])
    for idx in range(extend_amount):
        for col in range(len(risk_grid[row])):
            to_add = risk_grid[row][col]+idx
            if to_add > 9:
                to_add -= 9
            new_risk_grid[row].append(to_add)

for idx in range(1, extend_amount):
    for row in range(len(risk_grid)):
        new_row = [x+idx for x in new_risk_grid[row] ]
        for col in range(len(new_row)):
            if new_row[col] > 9:
                new_row[col] -= 9
        new_risk_grid.append(new_row)


risk_grid = new_risk_grid
# for row in range(len(risk_grid)):
#     for col in range(len(risk_grid[row])):
#         for idx in range(0):
#             new_risk = risk_grid[row][col]+idx+1
#             if new_risk == 10:
#                 new_risk = 1
#             risk_grid[row].append(new_risk)

# for row in risk_grid:
#     print(row)
# for row in new_risk_grid:
#     print(row)
# apply dijkstra's algorithm to find shortest path from [0][0] to [len(rows)-1][len(cols)-1]
start = (0, 0)
end = (len(risk_grid)-1, len(risk_grid[0])-1)
shortest_path = dijkstra(risk_grid, start, end)
print("SHORTEST PATH")
print(shortest_path)
print(len(shortest_path))
total = 0
for node in shortest_path[1:]:
    row = node[0]
    col = node[1]
    total += risk_grid[row][col]

print(total)

# return the "risk" of the shortest path

