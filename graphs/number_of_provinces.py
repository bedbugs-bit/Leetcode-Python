from collections import deque
from typing import List

class Solution:
    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for neighbour in range(size):
                if isConnected[city][neighbour]  == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for city in range(size):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces

    def findCircleBFS(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(size):
            if city not in visited:
                queue = deque([city])
                while queue:
                    curr = queue.popleft()
                    for neighbour in range(size):
                        if isConnected[curr][neighbour] == 1 and neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)

            provinces += 1

        return provinces

    graph = {
        0: [1, 3],
        1: [0,2, 4]
    }

    def dfs(self, graph, start):