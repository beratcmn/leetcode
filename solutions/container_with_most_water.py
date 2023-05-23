class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) > 10**5:
            return

        if len(height) == 2:
            return min(height)

        result = 0

        n1 = 0
        n2 = 1
        for a in height:
            for b in height[height.index(a)+1:]:
                if a > 10**4 or b > 10**4:
                    return
                x = n2 - n1
                y = min([a, b])
                r = x * y
                result = r if r > result else result
                n2 += 1
            n1 += 1
            n2 = n1 + 1

        return result
