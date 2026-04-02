class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

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
        