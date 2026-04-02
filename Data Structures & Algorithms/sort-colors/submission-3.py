class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.dutch_flag_sort(nums)
    
    def dutch_flag_sort(self, nums: List[int]) -> None:

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                swap(m, l)
                l += 1
            elif nums[m] == 2:
                swap(m, r)
                r -= 1
                m -= 1
            m += 1
    
    def count_sort(self, nums: List[int]) -> None:
        count = [0] * 3

        for n in nums:
            count[n] += 1
        
        i = 0
        for colour, c in enumerate(count):
            for _ in range(c):
                nums[i] = colour
                i += 1
        