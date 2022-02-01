# Completed
# Runtime: 180 ms, faster than 17.40% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.7 MB, less than 6.86% of Python3 online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < (len(nums)):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
                i = i - 1
            i = i + 1

        print(nums)
