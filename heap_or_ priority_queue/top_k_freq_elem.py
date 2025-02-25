from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return [item for item, freq in heapq.nlargest(k, count.items(), key = lambda x: x[1])]