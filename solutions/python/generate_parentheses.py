# Runtime 48 ms Beats 43.35%
# Memory 16.8 MB Beats 11.7%

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate_parenthesis_recursive(n, n, '', result)
        return result

    def generate_parenthesis_recursive(self, left: int, right: int, current: str, result: List[str]):
        if left == 0 and right == 0:
            result.append(current)
            return
        if left > 0:
            self.generate_parenthesis_recursive(left - 1, right, current + '(', result)
        if right > left:
            self.generate_parenthesis_recursive(left, right - 1, current + ')', result)
