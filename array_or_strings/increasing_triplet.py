class Solution:
    def increasing_triplet(self, nums):
        first_min = float('inf')
        second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False