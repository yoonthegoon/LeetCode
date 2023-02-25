# https://leetcode.com/problems/reverse-integer/


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        if x < 0:
            x *= -1
            negative = True
        else:
            negative = False

        output = int(str(x)[::-1])
        if output < 2**31:
            if negative:
                output *= -1
            return output
        return 0
