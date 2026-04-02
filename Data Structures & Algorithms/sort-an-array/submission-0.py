class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0

        while l < len(nums):
            small_i = l
            r = l + 1
            while r < len(nums):
                if nums[r] < nums[small_i]:
                    small_i = r
                r += 1
            tmp = nums[l]
            nums[l] = nums[small_i]
            nums[small_i] = tmp
            l += 1
        return nums
        