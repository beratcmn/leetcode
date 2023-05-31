# Runtime 537 ms Beats 89.66%
# Memory 30.9 MB Beats 51.59%

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
