class Solution:
    def productExceptSelf(self, nums):
        size = len(nums)

        left_product = [1] * size
        right_product = [1] * size
        ans = [0] * size

        for i in range(1, size):
            left_product[i] = left_product[i -1] * nums[i-1]