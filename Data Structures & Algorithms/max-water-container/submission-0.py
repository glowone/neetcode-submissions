from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max = 0


        while left < right: 
            if (min(heights[left], heights[right])*abs(right - left) > max):
                max = min(heights[left], heights[right])*abs(right - left)
            elif (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        return max
                