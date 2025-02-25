adj = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

def count_edges(adj):
    total = sum(len(neigh) for neigh in adj.values())

    # each undirected edge appears twice
    return  total // 2


