from solutions.merge_sorted_array import Solution as merge_sorted_array

solution = merge_sorted_array()

result = solution.merge(
    nums1=[1,2,3,0,0,0], 
    m=3,
    nums2=[2,5,6],
    n=3
    )

print(result)