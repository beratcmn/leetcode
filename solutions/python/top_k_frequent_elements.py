# Runtime 1791 ms Beats 5%
# Memory 21.2 MB Beats 44.86%

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        nums_set = set(nums)

        for n in nums_set:
            count_dict[n] = nums.count(n)

        count_value_list = sorted(sorted(count_dict.items()), key=lambda x: x[1], reverse=True)

        result = []
        for c, v in count_value_list[:k]:
            result.append(c)

        return result
