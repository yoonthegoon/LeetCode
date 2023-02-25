# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> int:
        if s != s[::-1]:
            return False
        return True

    @staticmethod
    def get_substrings(s: str, r: int) -> list[str]:
        if r == 1:
            return list(s)

        substrings = []
        for i, _ in enumerate(s[: -r + 1]):
            substrings.append(s[i : i + r])
        return substrings

    def find_palindromes(self, s: str):
        for i in reversed(range(len(s))):
            substrings = self.get_substrings(s, i + 1)
            for substring in substrings:
                if self.is_palindrome(substring):
                    return substring

    def longestPalindrome(self, s: str) -> str:
        return self.find_palindromes(s)
