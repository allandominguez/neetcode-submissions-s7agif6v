class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()
        for i, num in enumerate(nums):
            num_index[num] = i
        
        for i, num in enumerate(nums):
            remaining = target - num
            if (remaining in num_index) and (num_index[remaining] != i):
                return [i, num_index[remaining]]
        
        return [0, 0]