// Runtime 148 ms Beats 41.17%
// Memory 44 MB Beats 36.93%

namespace LetterCombinationsOfAPhoneNumber {
    public class Solution {
        public IList<string> LetterCombinations(string digits) {
            if (digits == "")
                return new List<string>();

            Dictionary<char, List<char>> keyboard = new Dictionary<char, List<char>>()
        {
            { '2', new List<char> { 'a', 'b', 'c' } },
            { '3', new List<char> { 'd', 'e', 'f' } },
            { '4', new List<char> { 'g', 'h', 'i' } },
            { '5', new List<char> { 'j', 'k', 'l' } },
            { '6', new List<char> { 'm', 'n', 'o' } },
            { '7', new List<char> { 'p', 'q', 'r', 's' } },
            { '8', new List<char> { 't', 'u', 'v' } },
            { '9', new List<char> { 'w', 'x', 'y', 'z' } }
        };

            List<string> pairs = new List<string>();

            void Backtrack(string combination, string nextDigits) {
                if (nextDigits.Length == 0) {
                    pairs.Add(combination);
                } else {
                    foreach (char letter in keyboard[nextDigits[0]]) {
                        Backtrack(combination + letter, nextDigits.Substring(1));
                    }
                }
            }

            Backtrack("", digits);
            return pairs;
        }
    }
}