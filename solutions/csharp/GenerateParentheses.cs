// Runtime 129 ms Beats 87.29%
// Memory 45.9 MB Beats 58.67%

namespace GenerateParentheses {
    public class Solution {
        public IList<string> GenerateParenthesis(int n) {
            var result = new List<string>();
            GenerateParenthesisRecursive(n, n, "", result);
            return result;
        }

        void GenerateParenthesisRecursive(int left, int right, string current, List<string> result) {
            if (left == 0 && right == 0) {
                result.Add(current);
                return;
            }

            if (left > 0) {
                this.GenerateParenthesisRecursive(left - 1, right, current + '(', result);
            }
            if (right > left) {
                this.GenerateParenthesisRecursive(left, right - 1, current + ')', result);
            }
        }
    }
}