# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        table = [["" for _ in range(len(s))] for _ in range(num_rows)]

        i, r, c = 0, 0, 0
        while s:
            table[r][c] = s[0]
            s = s[1:]
            i += 1
            if 0 < i % (2 * (num_rows - 1)) < num_rows:
                r += 1
            else:
                r -= 1
                c += 1
        output = ""
        for row in table:
            output += "".join(row)
        return output
