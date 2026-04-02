from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # do a count of n in nums
        # use a heap to keep track of the K max values
            # by heap-popping when the heap is greater than K
        num_count = defaultdict(int)
        for n in nums:
            num_count[n] += 1
        min_heap = []
        for n, count in num_count.items():
            heappush(min_heap, (count, n))
            if len(min_heap) > k:
                heappop(min_heap)
        return [n for _, n in min_heap]
        