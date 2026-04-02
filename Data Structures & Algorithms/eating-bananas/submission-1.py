class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = right = max(piles)
        left = 1
        while left <= right:
            mid = (left + right) // 2
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / mid)
                if time_taken > h:
                    break
            if time_taken <= h:
                minimum = mid
                right = mid - 1
            else:
                left = mid + 1
        return minimum