from typing import List

from prefix_sum.sums_counts import prefix_sum


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        size = len(gain)
        prefix_arr = [0] * (size +1)

        for i in range(1, size +1):
            prefix_arr[i] = prefix_arr[i-1] + gain[i-1]

        return max(prefix_arr)



