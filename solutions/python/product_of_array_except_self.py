# Runtime 230 ms Beats 82.91%
# Memory 23.5 MB Beats 64.2%

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= prod
            prod *= nums[i]

        return result
