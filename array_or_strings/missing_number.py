class Solution:
    def missing_number(self, nums):
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i
        if nums[-1] != len(nums):
            return len(nums)

    def alternate_solu_missing_num(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)