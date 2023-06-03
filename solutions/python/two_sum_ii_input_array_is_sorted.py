# Runtime 132 ms Beats 77.8%
# Memory 17.3 MB Beats 38.66%

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(numbers):
            remaining = target - num
            if remaining in num_dict:
                return [num_dict[remaining] + 1, i + 1]
            num_dict[num] = i
