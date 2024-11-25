# array of edges, directed graph [[start, end]]
nodes = 5
arrofEdges = [[0,1], [1, 2], [0,3], [3, 4]]

# convert array of edges into adjacency matrix
adjMatrix = []
for i in range(nodes):
    adjMatrix.append([0] * nodes)

for start, end in arrofEdges:
    adjMatrix[start][end] = 1

    # if this graph is undirected, uncomment the next line
    # adjMatrix[end][start] = 1

# convert the array of edges into an adjacency list

from collections import defaultdict

adjList = defaultdict(list)

for start, end in arrofEdges:
    adjList[start].append(end)

    # uncomment the next line if the graph is undirected
    # adjList[end].append(start)

# Dfs with recursion
def dfs_recursive(node):
    print(node)

    for nei_node in adjList[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)



source = 0
seen = set()
seen.add(source)
dfs_recursive(source)

# DFS with a stack

stack = [source]

while stack:
    node = stack.pop()
    print(node)

    for nei_node in adjList[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)
