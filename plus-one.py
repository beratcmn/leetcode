# Completed
# Runtime: 32 ms, faster than 82.37% of Python3 online submissions for Plus One.
# Memory Usage: 13.9 MB, less than 87.57% of Python3 online submissions for Plus One.


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = 0
        answer = []

        i = 0
        while i < len(digits):
            num = num + ((10 ** i) * digits[-i - 1])
            i = i + 1

        for n in str(num + 1):
            answer.append(n)

        return answer
