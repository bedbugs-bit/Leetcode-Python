from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        max_length = 0
        size = len(arr)

        for peak in range(1, size - 1):
            # check if arr[peak] is a peak
            left, right = peak - 1, peak + 1
            if arr[peak] > arr[left] and arr[peak] > arr[right]:

                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                while right < size - 1 and arr[right] > arr[right + 1]:
                    right += 1

                max_length = max(max_length, right - left + 1)

        return max_length






