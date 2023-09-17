# Runtime 1154ms Beats 23.74%
# Memory 16.20MB Beats 87.23%

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        k = j + 1
                        l = len(nums) - 1
                        while k < l:
                            if nums[i] + nums[j] + nums[k] + nums[l] == target:
                                quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                                k += 1
                                l -= 1
                                while k < l and nums[k] == nums[k - 1]:
                                    k += 1
                                while k < l and nums[l] == nums[l + 1]:
                                    l -= 1
                            elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                                k += 1
                            else:
                                l -= 1
        return quadruplets
