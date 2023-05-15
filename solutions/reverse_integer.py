# Runtime 32 ms Beats 79.6%
# Memory 13.6 MB Beats 99.88%

class Solution:
    def reverse(self, x: int) -> int:
        mark = 0
        if x > 0:
            mark = 1
        elif x < 0:
            mark = -1
        x = abs(x)
        x = str(x)
        liste = list(x)
        liste.reverse()
        y = ""
        y = y.join(liste)
        y = y.strip("0")
        try:
            y = int(y)
            y = y * mark
            if y > (2 ** 31) - 1:
                return 0
            elif y < -(2 ** 31):
                return 0
            return y
        except:
            return 0            
        
            