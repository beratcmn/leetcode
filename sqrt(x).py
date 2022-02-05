# Completed
# Runtime: 44 ms, faster than 63.94% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.9 MB, less than 94.88% of Python3 online submissions for Sqrt(x).

from math import log10


class Solution:
    def mySqrt(self, x: int) -> int:

        return 0 if x == 0 else int(10**(log10(x)/2))
