class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        lower = set()
        upper = set()

        max_seq = curr_seq = 1
        for num in nums:
            if num - 1 in nums:
                continue
            while num + 1 in nums:
                curr_seq += 1
                if curr_seq > max_seq:
                    max_seq = curr_seq
                num += 1
            curr_seq = 1
        
        return max_seq
                
