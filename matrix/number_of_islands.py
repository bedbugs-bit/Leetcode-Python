from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:  # Fix for empty input
            return 0

        def bfs(ith, jth):
            q = deque()
            visited.add((ith, jth))
            q.append((ith, jth))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    res_row, res_col = row + dr, col + dc

                    # Fix boundary checks and land check
                    if (0 <= res_row < rows_len and 0 <= res_col < cols_len and
                            (res_row, res_col) not in visited and grid[res_row][res_col] == '1'):
                        q.append((res_row, res_col))
                        visited.add((res_row, res_col))

        count = 0
        rows_len = len(grid)
        cols_len = len(grid[0])
        visited = set()

        for i in range(rows_len):
            for j in range(cols_len):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    count += 1  # Each BFS run finds one island

        return count

    def numIslandsDFS(self, grid):
        if not grid or not grid[0]:
            return 0

        len_rows, len_cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            # check the boundaries
            if i < 0 or i >= len_rows or j < 0 or j >= len_cols or grid[i][j] == '0':
                return

            grid[i][j] = '0' # mark as visited

            # explore all 4 directions
            dfs(i + 1, j) # up
            dfs(i - 1, j) # down
            dfs(i, j + 1) # right
            dfs(i, j - 1) # left

        for r in range(len_rows):
            for c in range(len_cols):
                if grid[r][c] == '1': # found and island
                    dfs(r,c)
                    count += 1

        return count

