class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a, 2)
        n2 = int(b, 2)

        return bin(n1 + n2)[2:]