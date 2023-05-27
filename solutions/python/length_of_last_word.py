# Runtime: 44 ms, faster than 35.14 % of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.8 MB, less than 98.88 % of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
