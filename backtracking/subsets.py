from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path.copy())  # shallow copy

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)

                path.pop()

        result = []
        backtrack(0, [])
        # O((2^n) * n) the copy function add a 0(n) complexity
        # O((2^n) * n) calls the recursive function before it returns
        return result

