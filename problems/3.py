# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    @staticmethod
    def count_non_repeating(s: str) -> int:
        count = 0
        visited_characters = {}
        for character in s:
            if visited_characters.get(character):
                break
            count += 1
            visited_characters[character] = True
        return count

    def iterate_characters(self, s: str):
        longest = 0
        while s:
            count = self.count_non_repeating(s)
            if count > longest:
                longest = count
            s = s[1:]
        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.iterate_characters(s)
