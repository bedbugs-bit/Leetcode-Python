from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for indx, val in enumerate(nums):

            if indx > 0 and  val == nums[indx -1]:
                continue

            left = indx + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = val + nums[left] + nums[right]

                if curr_sum > 0:
                    right -= 1

                elif curr_sum < 0:
                    left += 1

                else:
                    res.append([val, nums[left], nums[right]])

                    # skip duplicate values after finding a valid triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                    # O(n**2) time complexity
                    # 0(n) space complexity

        return res

    def solu_hash_map(self, nums):
        res = set()
        nums.sort()

        for i in range(len(nums)):
            target = nums[i]
            map = {}

            for j in range(i+1, len(nums)):
                complement  = -(target + nums[j])

                if complement in map:
                    res.add((nums[i], complement, nums[j]))

                map[nums[j]] += 1



        # O(n**2) time complexity
        # 0(n) space
        return  list(res)







