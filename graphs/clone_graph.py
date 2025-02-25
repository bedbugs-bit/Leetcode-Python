from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph_dfs(self, node: Node) -> Optional[Node]:
        if not node:
            return None
        # maps original nodes to their clones
        clones = {}

        def dfs(curr):
            if curr in clones:
                return clones[curr]

            # create a clone
            clone = Node(curr.val)

            # map the Node to its clone
            clones[curr] = clone

            # recursively clone all the neighbours
            for neigh in curr.neighbors:
                clone.neighbors.append(dfs(neigh))

            return clone

        return dfs(node)


    def clone_graph_bfs(self, node):
        if not node:
            return None

        clones = {}  # Dictionary to store cloned nodes
        q = deque([node])  # Queue for BFS

        # Clone the first node and store it
        clones[node] = Node(node.val)

        while q:
            curr = q.popleft()
            print(f"Processing Node: {curr.val}")

            for neighbour in curr.neighbors:
                if neighbour not in clones:
                    clones[neighbour] = Node(neighbour.val)
                    q.append(neighbour)
                    print(f"Cloning Node {neighbour.val} and adding it to the queue.")

                # Append the cloned neighbor to the clone's neighbor list
                clones[curr].neighbors.append(clones[neighbour])
                print(f"Adding edge {curr.val} -> {neighbour.val} in cloned graph.")

        return clones[node]