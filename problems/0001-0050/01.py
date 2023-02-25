# https://leetcode.com/problems/two-sum/


class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            try:
                j = nums.index(target - num)
            except ValueError:
                j = i
            if j != i:
                return [i, j]
