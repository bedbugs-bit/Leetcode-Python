from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs():
            pass

        count = 0
        rows = len(grid)
        cols = len(grid[0])

