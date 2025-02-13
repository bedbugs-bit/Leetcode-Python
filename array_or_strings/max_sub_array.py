from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        return  max_sum

    def max_sub_arr_dp(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            dp[i] = max(num, dp[i-1] + num)

        return max(dp)

