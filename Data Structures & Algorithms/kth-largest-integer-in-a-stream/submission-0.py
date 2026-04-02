class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        heapq.heapify(nums)
        self._heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        return heapq.nlargest(self._k, self._heap)[self._k - 1]
