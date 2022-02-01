# Completed
# Runtime: 6770 ms, faster than 6.67 % of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 67.33 % of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for n in nums:
            new_list = []
            new_list.extend(nums)
            new_list[new_list.index(n)] = 9999

            for n2 in new_list:
                if (n + n2) == target:
                    return [nums.index(n), new_list.index(n2)]
