# prefix sum and hash map problem
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros, ones = 0,0
        res = 0

        diff_to_index_map = {}
        for i, val in enumerate(nums):
            if val == 0:
                zeros += 1
            else:
                ones += 1

            if ones - zeros not in diff_to_index_map:
                diff_to_index_map[ones - zeros] = i

            if ones == zeros:
                res = ones + zeros
            else:
                idx = diff_to_index_map[ones - zeros]
                res = max(res, i - idx)

        return res



