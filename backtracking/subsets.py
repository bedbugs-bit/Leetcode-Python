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
        return result

