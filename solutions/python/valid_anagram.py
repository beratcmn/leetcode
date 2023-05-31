# Runtime 75 ms Beats 19.47%
# Memory 17.5 MB Beats 5.32%

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t
