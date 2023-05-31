# Runtime 618 ms Beats 5.15%
# Memory 28.4 MB Beats 92.53%

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        duplicates = []
        for i, n in enumerate(nums[0:len(nums)-1]):
            if len(duplicates) > 0:
                break
            if n == nums[i+1]:
                duplicates.append(n)

        return True if len(duplicates) > 0 else False
