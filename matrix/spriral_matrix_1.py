from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:

            # step 1
            res += matrix.pop(0)

            # step 2
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            # step 3
            if matrix:
                res += (matrix.pop()[::-1])

            # step 4
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res
