# https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
