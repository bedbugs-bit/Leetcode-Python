from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed.insert(0, 0)
        flowerbed.append(0)
        flower_count = 0

        for i in range(1, len(flowerbed) -1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                flower_count += 1

        return  n <= flower_count

    def can_placeFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        flowers = 0
        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == (length - 1) or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                flowers += 1
        return n <= flowers

