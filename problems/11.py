# https://leetcode.com/problems/container-with-most-water/


class Solution:
    @staticmethod
    def maxArea(height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
