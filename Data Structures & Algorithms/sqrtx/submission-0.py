class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = (l + r) // 2
            exp = m * m
            if exp == x:
                return m
            if exp > x:
                r = m - 1
            else:
                l = m + 1
        
        return r
        