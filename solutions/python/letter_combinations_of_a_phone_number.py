# Runtime 31 ms Beats 86.32%
# Memory 16.5 MB Beats 5.46%

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        keyboard = {
            "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
            "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                pairs.append(combination)
            else:
                for letter in keyboard[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        pairs = []
        backtrack("", digits)
        return pairs
