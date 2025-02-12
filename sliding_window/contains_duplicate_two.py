from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            if i > k:
                seen.remove(num[i-k-1])

            if num in seen: return  True

            seen.add(num)

        # O(n) time complexity, 0(n) space complexity
        return False

    def map_solu(self, nums, k):
        map = {}

        for i, val in enumerate(nums):
            if val in map and i - map[val] <= k:
                return True

            map[val] = i

        return False





