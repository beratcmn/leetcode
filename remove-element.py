# Completed
# Runtime: 53 ms, faster than 27.02 % of Python3 online submissions for Remove Element.
# Memory Usage: 13.9 MB, less than 92.99 % of Python3 online submissions for Remove Element.


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
                i = i - 1
            i = i + 1
        print(nums)
