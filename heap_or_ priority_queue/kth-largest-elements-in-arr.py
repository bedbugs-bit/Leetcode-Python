import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # O(n) for the heap construction, 0(log k) for extracting min max values n time
        # O(n log n) total time
        return heapq.nlargest(k, nums)[-1]




