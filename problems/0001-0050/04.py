# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        middle_index = len(nums) // 2
        return (nums[middle_index] + list(reversed(nums))[middle_index]) / 2
