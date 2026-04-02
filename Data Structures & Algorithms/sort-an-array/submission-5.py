class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heap_sort(nums)

    def heap_sort(self, nums: List[int]) -> List[int]:
        max_heap = MaxHeap(nums)
        return max_heap.sort()

    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        left = nums[:len(nums) // 2]
        arr1 = self.merge_sort(left)
        right = nums[len(nums) // 2:]
        arr2 = self.merge_sort(right)

        return self.merge(arr1, arr2)
    
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        i = j = 0

        while (i < len(arr1)) and (j < len(arr2)):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        
        return res
        
class MaxHeap:
    def __init__(self, nums: List[int]):
        self.heap = nums    # not copying for space optimisation
        self._build_max_heap()
    
    def _build_max_heap(self):
        """Will operate on self.heap for space optmisation"""
        non_leaf_node = (len(self.heap) // 2) - 1

        while non_leaf_node >= 0:
            self.heapify(non_leaf_node)
            non_leaf_node -= 1
    
    def heapify(self, node: Optional[int] = 0, end: Optional[int] = None):
        """Operates on self.heap"""
        if end is None:
            end = len(self.heap) - 1

        l = (2 * node) + 1
        r = (2 * node) + 2
        largest = node

        if l <= end and self.heap[l] > self.heap[largest]:
            largest = l
        if r <= end and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != node:
            self.heap[node], self.heap[largest] = self.heap[largest], self.heap[node]
            self.heapify(largest, end)
    
    def sort(self) -> List[int]:
        """Will operate on self.heap for space optmisation, meaning we lose the max_heap when called."""
        end = len(self.heap) - 1

        while end > 0:
            self.heap[0], self.heap[end] = self.heap[end], self.heap[0]
            end -= 1
            self.heapify(end=end)
        
        return self.heap

