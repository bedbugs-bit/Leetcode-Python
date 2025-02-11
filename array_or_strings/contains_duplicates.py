class Solution:
    def contains_duplicates(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False