from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        size = len(nums)
        window_min_length = float('inf')
        k = 0
        curr_sum = 0

        for i in range(size):
            curr_sum += nums[i]

            while curr_sum >= target:
                window_min_length = min(window_min_length, i - k + 1)
                curr_sum -= nums[k]
                k += 1

        if window_min_length == float('inf'):
            window_min_length = 0

        return window_min_length

