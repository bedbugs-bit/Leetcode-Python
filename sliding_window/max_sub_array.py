from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1 and len(nums) == 1:
            return nums[0]

        if k == 1:
             return max(nums)


        window_max = sum(nums[:k])
        max_sum = window_max

        for i in range(len(nums)-k):
            window_max = (window_max - nums[i] + nums[i+k])
            max_sum = max(max_sum, window_max)

        return max_sum / k
