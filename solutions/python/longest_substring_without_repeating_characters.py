# Runtime 530 ms Beats 11.79%
# Memory 16.4 MB Beats 10.46%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        longest = 1
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    break
                else:
                    if j - i + 1 > longest:
                        longest = j - i + 1
        return longest