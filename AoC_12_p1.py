class Graph: 
    def __init__(self, edges, vertices): 
        self.edges = edges
        self.vertices = vertices
        self.neighbors = dict()
        cur_neigbor_set = set()
        for vertex in self.vertices:
            cur_neigbor_set = set()
            for edge in edges:
                node1, node2 = edge
                if node1 == vertex:
                    cur_neigbor_set.add(node2)
                elif node2 == vertex:
                    cur_neigbor_set.add(node1)
            self.neighbors[vertex] = cur_neigbor_set

    def get_all_paths_helper(self, start, end, visited, cur_path, all_paths):
        visited[start] = True
        cur_path.append(start)

        if start == end: 
            all_paths.append(cur_path.copy())
        else: 
            for vertex in self.neighbors[start]:
                if visited[vertex] == False or vertex.upper() == vertex :
                    self.get_all_paths_helper(vertex, end, visited, cur_path, all_paths)
        cur_path.pop()
        visited[start] = False

    def get_all_paths(self, start, end): 
        all_paths = list()
        cur_path = list()
        visited = dict()
        for vertex in self.vertices:
            visited[vertex] = False
        self.get_all_paths_helper(start, end, visited, cur_path, all_paths)

        return all_paths

edges = list()
vertices = set()

with open("AoC_12_input.txt") as f:
    while True:
        line = f.readline()
        if line == '':
            break
        if line[-1] == '\n':
            line = line[:-1]
        edges.append(set(line.split('-')))
        for vertex in line.split('-'):
            vertices.add(vertex)

# print(edges)
# print(vertices)

cur_graph = Graph(edges, vertices)

paths = cur_graph.get_all_paths('start', 'end')
# print(paths) 
# for path in pa
#     print(path)

print(len(paths))
# organize data as a graph
# graph has vertices and edges

# find all paths from start to end
    # small caves can only be in the path once. 
    # large caves can be in the path any number of times

# return the number of paths that fit that criteria. 