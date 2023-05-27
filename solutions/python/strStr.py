# Runtime: 32 ms, faster than 90.77 % of Python3 online submissions for Implement strStr().
# Memory Usage: 14.2 MB, less than 96.56 % of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
