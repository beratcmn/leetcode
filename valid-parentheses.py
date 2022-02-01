# Completed
# Runtime: 36 ms, faster than 53.76% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 22 MB, less than 6.91% of Python3 online submissions for Valid Parentheses.

class Solution:
    def removeCorrectPairs(self, s: str):
        inpt = s
        correct_pairs = ["()", "[]", "{}"]

        for c in correct_pairs:
            inpt = inpt.replace(c, "")

        for c in correct_pairs:
            if c in inpt:
                inpt = self.removeCorrectPairs(inpt)

        return inpt

    def isValid(self, s: str) -> bool:
        return self.removeCorrectPairs(s) == ""
