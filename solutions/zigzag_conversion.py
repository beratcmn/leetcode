# Runtime 81 ms Beats 28.25%
# Memory 16.4 MB Beats 21.33%

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        sArray = list(s)
        result = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < len(sArray):
                    result += sArray[j]
                    j += 2 * numRows - 2
            else:
                j = i
                while j < len(sArray):
                    result += sArray[j]
                    j += 2 * numRows - 2 - 2 * i
                    if j < len(sArray):
                        result += sArray[j]
                        j += 2 * i
        return result
