# Runtime 51 ms Beats 20.67%
# Memory 16.4 MB Beats 10.49%

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        if m == 0 and n != 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        elif m != 0 and n == 0:
            nums1 = nums1
        elif m != 0 and n != 0:
            joined_ul = nums1[0:m] + nums2
            joined_ul.sort()
        
            for i in range(len(nums1)):
                nums1[i] = joined_ul[i]
