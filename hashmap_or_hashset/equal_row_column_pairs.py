from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size = len(grid)
        row_count = {}

        # count the rows
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1

        count = 0
        for col_index in range(size):
            column = tuple(grid[row_index][col_index] for row_index in range(size))

            if column in row_count:
                count += row_count[column]

        return count
