# Runtime 408 ms Beats 71.39%
# Memory 32.2 MB Beats 14.93%

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))

        if len(nums) == 1:
            return 1

        longest_seq = 1
        current_seq = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_seq += 1
            else:
                longest_seq = max(longest_seq, current_seq)
                current_seq = 1

        return max(longest_seq, current_seq)
