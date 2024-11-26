from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() # sort the array
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operations += 1
                left += 1
                right -= 1

            elif current_sum < k:
                # move the left pointer to increase the sum
                left += 1
            else:
                # move the right pointer to reduce the sum
                right -= 1

        return operations


