class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heap_sort(nums)

    def heap_sort(self, nums: List[int]) -> List[int]:
        max_heap = self._build_max_heap(nums)
        # extract and heapify
        end = len(nums) - 1
        while end > 0:
            # swap top and end
            self._swap(nums, 0, end)
            # decrement end
            end -= 1
            # heapify the top
            self.heapify(nums, 0, end)
        return nums
    
    def _swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    
    def _build_max_heap(self, nums: List[int]) -> List[int]:
        # get last non-leaf node index in array
        non_leaf_node = (len(nums) // 2) - 1
        while non_leaf_node >= 0:
            self.heapify(nums, non_leaf_node, len(nums) - 1)
            non_leaf_node -= 1
        print(nums)
        return nums
    
    def heapify(self, nums: List[int], node: int, end: int):
        largest = node
        l = 2 * node + 1
        r = 2 * node + 2

        if l <= end and nums[l] > nums[largest]:
            largest = l
        if r <= end and nums[r] > nums[largest]:
            largest = r
        
        if largest != node:
            self._swap(nums, node, largest)
            self.heapify(nums, largest, end)


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
        