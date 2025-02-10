# Number 1 Convert Array of Edges -> Adjacency Matrix
nodes = 5
arr_of_edges = [[0,1], [1,2], [0,3], [3,4]]

# init the adj matrix
adj_matrix = [[0] * nodes for _ in range(nodes)]

# Populate the matrix
for start, end in arr_of_edges:
    adj_matrix[start][end] = 1 # directed graph

    # uncomment for undirected graph
    # adj_matrix[end][start]

# print out the adjacency matrix
print("Adjacency matrix")
for row in adj_matrix:
    print(row)

# Number 2  Convert array of edges to adjacency list
from collections import defaultdict
adj_list = defaultdict(list)

for start, end in arr_of_edges:
    adj_list[start].append(end)

print("Adjacency List")
for key, val in adj_list.items():
    print(f"{key}: {val}")

# Number 3 Convert adjacency matrix -> Adjacency List
adj_list_from_matrix = defaultdict(list)

for i in range(nodes):
    for j in range(nodes):
        if adj_matrix[i][j] == 1:
            adj_list_from_matrix[i].append(j)

print("Adjacency list from matrix")
for key, val in adj_list_from_matrix.items():
    print(f"{key}: {val} ")


# Adjacency matrix -> array of edges
adj_edges = []

for i in range(nodes):
    for j in range(nodes):
        if adj_matrix[i][j] == 1:
            adj_edges.append([i, j])

print(adj_edges)


adj_matrix_from_list = [[0] * nodes for _ in range(nodes)]

for start, neighbors in adj_list.items():
    for end in neighbors:
        adj_matrix_from_list[start][end] = 1

# Print adjacency matrix
for row in adj_matrix_from_list:
    print(row)

