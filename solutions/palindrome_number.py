# Runtime 68 ms Beats 49.95%
# Memory 13.9 MB Beats 29.8%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        return temp == rev