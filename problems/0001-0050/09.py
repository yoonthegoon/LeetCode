# https://leetcode.com/problems/palindrome-number/


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        return False
