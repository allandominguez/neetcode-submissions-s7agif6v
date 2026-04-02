class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        last_valid = l

        while l <= r:
            mid = (l + r) // 2
            exp = (mid * mid)
            if exp == x:
                return mid
            elif exp < x:
                l = mid + 1
                last_valid = mid
            else:
                r = mid - 1
        
        return last_valid
        