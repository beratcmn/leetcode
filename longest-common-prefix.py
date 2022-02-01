# Completed
# Runtime: 55 ms, faster than 27.56% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 99.51% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0

        while all(s[0:i] == strs[0][0:i] for s in strs):
            if len(strs) == 1:
                return strs[0]

            i = i + 1

            if any(s == "" for s in strs):
                return ""

            if all(strs[0] == s for s in strs):
                return strs[0]

        return strs[0][0:i-1]
