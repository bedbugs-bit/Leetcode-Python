from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array
        arr.sort()
        res = []

        # Initialize min_diff as positive infinity
        min_diff = float('inf')

        # Find the minimum absolute difference
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        # Find all pairs with min_diff
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                res.append([arr[i - 1], arr[i]])

        return res
