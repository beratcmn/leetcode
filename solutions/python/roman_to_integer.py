# Runtime 87 ms Beats 5.12%
# Memory 13.8 MB Beats 75.17%

class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        ans = 0
        for i in range(len(s)-1, -1, -1):
            num = pairs[s[i]]
            if 4 * num < ans:
                ans -= num
            else:
                ans += num
        return ans