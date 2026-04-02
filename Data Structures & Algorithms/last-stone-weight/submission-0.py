from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            remaining = first - second
            if remaining < 0:
                heappush(stones, remaining)
        return -heappop(stones) if stones else 0
        