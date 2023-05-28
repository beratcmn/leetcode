// Runtime 70 ms Beats 62.30%
// Memory 41 MB Beats 10.97%

namespace StringtoIntegerAtoi {
    public class Solution {
        public int MyAtoi(string s) {
            s = s.Trim();

            if (string.IsNullOrEmpty(s)) {
                return 0;
            }

            int sign = 1;

            if (s[0] == '-') {
                sign = -1;
                s = s.Substring(1);
            } else if (s[0] == '+') {
                sign = 1;
                s = s.Substring(1);
            }

            char[] sArray = s.ToCharArray();

            if (sArray.Length == 0) {
                return 0;
            }

            string result = "";

            foreach (char c in sArray) {
                if (char.IsNumber(c)) {
                    result += c;
                } else {
                    break;
                }
            }

            if (string.IsNullOrEmpty(result)) {
                return 0;
            }

            int upLimit = (int)Math.Pow(2, 31) - 1;
            int bottomLimit = -(int)Math.Pow(2, 31);
            int parsedResult;
            try {
                parsedResult = checked(int.Parse(result)) * sign;
            } catch (OverflowException) {
                parsedResult = sign == 1 ? upLimit : bottomLimit;
            }

            return parsedResult;
        }
    }
}