# Runtime 49 ms Beats 84.5%
# Memory 16.7 MB Beats 71.87%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = self.remove_non_alphanumeric(s)
        return text == text[::-1]

    def remove_non_alphanumeric(self, text: str):
        clean_text = ''
        for char in text:
            if char.isalnum():
                clean_text += char
        return clean_text.lower()
