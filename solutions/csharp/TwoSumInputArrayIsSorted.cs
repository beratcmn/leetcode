// Runtime 150 ms Beats 79.62%
// Memory 46.6 MB Beats 28.40%

namespace TwoSumInputArrayIsSorted {
    public class Solution {
        public int[] TwoSum(int[] numbers, int target) {
            Dictionary<int, int> numDict = new Dictionary<int, int>();

            for (int i = 0; i < numbers.Length; i++) {
                int remaining = target - numbers[i];

                if (numDict.ContainsKey(remaining)) {
                    return new int[] { numDict[remaining] + 1, i + 1 };
                }

                numDict[numbers[i]] = i;
            }

            return new int[0];
        }
    }
}