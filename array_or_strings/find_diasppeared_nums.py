from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)

        res = []

        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                res.append(i)

        # O(n) time, O(n) space
        return res

    def solu_constant_time(self, nums):
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1

            if nums[temp] > 0:
                nums[temp] *= -1
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res

