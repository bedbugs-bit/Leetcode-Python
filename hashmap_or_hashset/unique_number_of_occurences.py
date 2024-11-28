from typing import List
from collections import  Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # count the occurrences using dictionary/hash map
        count_map = {}
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1

        # check if the counts are unique
        occurrences = set()
        for count in count_map.values():
            if count in occurrences:
                return False
            occurrences.add(count)

        return True

    def unique_occurrences(self, arr: List[int]) -> bool:
        # Count the occurrences using Counter
        count_map = Counter(arr)

        # Check if the counts are unique
        return len(set(count_map.values())) == len(count_map.values())








