# Runtime 58 ms Beats 29.37%
# Memory 17.1 MB Beats 19.1%

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)