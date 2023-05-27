# Runtime 51 ms Beats 18.98%
# Memory 16.3 MB Beats 22.84%

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        sign = 1

        if s[0:1] == "-":
            sign = -1
            s = s[1:]
        elif s[0:1] == "+":
            sign = 1
            s = s[1:]

        sArray = list(s)

        if len(sArray) == 0:
            return 0

        result = ""
        for c in sArray:
            if c.isnumeric():
                result += c
            else:
                break

        if result == "":
            return 0

        result = int(result) * sign
        upLimit = (2**31) - 1
        bottomLimit = -2**31
        result = upLimit if result > upLimit else bottomLimit if result < bottomLimit else result

        return int(result)
