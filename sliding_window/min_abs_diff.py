from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        res = []
        arr.sort()

        min_diff = int('-inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                res.append([arr[i-1], arr[i]])


