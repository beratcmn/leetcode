// Runtime 78 ms Beats 81.14%
// Memory 40.9 MB Beats 21.79%

namespace IsAnagram {
    public class Solution {
        public bool IsAnagram(string s, string t) {
            char[] sChars = s.ToCharArray();
            char[] tChars = t.ToCharArray();

            Array.Sort(sChars);
            Array.Sort(tChars);

            return new string(sChars) == new string(tChars);
        }
    }
}