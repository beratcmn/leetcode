# Runtime 63 ms Beats 54.38%
# Memory 17.6 MB Beats 5.32%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
