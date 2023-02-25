# https://leetcode.com/problems/regular-expression-matching


import re


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        return re.fullmatch(p, s)
