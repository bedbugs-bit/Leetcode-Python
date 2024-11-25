from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)


            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

