class Solution:
    def product_except_self(self, nums):
        size = len(nums)
        answer = [1] * size

        # Fill in the prefix sum
        prefix_product = 1
        for i in range(size):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(size -1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer

