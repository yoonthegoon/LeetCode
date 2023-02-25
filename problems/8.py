# https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            negative = False
            s = s[1:]
        else:
            negative = False
        output = ""
        for i in range(len(s)):
            if s[i].isdigit():
                output += s[i]
            else:
                break
        if output:
            output = int(output)
            if negative:
                output *= -1
            if output < -(2**31):
                return -(2**31)
            elif output > 2**31 - 1:
                return 2**31 - 1
            return output
        return 0
