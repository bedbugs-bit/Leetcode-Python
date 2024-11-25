from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [(candy + extraCandies >= max_candies) for candy in candies]
        return result

    def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandy = 0
        for num in candies:
            if maxCandy < num:
                maxCandy = num
        for num in candies:
            if num + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)

        return result