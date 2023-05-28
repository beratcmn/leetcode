// Runtime 370 ms Beats 5.6%
// Memory 60.5 MB Beats 5.25%

namespace TwoSum {
    public class Solution {
        public int[] TwoSum(int[] nums, int target) {
            for (int i = 0; i < nums.Length; i++) {
                int[] newList = new int[nums.Length];
                Array.Copy(nums, newList, nums.Length);
                newList[Array.IndexOf(nums, nums[i])] = 9999;

                for (int j = 0; j < newList.Length; j++) {
                    if (nums[i] + newList[j] == target) {
                        return new int[] { i, Array.IndexOf(newList, newList[j]) };
                    }
                }
            }

            return new int[] { };

        }
    }

}