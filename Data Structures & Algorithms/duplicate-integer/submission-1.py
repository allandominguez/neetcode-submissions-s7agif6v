class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums.sort()
        last = nums[0]
        for num in nums[1:]:
            if num == last:
                return True
            last = num
        return False
         