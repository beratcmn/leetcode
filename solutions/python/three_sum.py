# Runtime 1512 ms Beats 51.57%
# Memory 20.5 MB Beats 36.74%

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums: List[int], i: int, result: List[List[int]]):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                result.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
