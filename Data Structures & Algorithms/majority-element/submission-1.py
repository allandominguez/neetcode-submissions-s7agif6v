class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        max_count = max_n = 0

        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > max_count:
                max_count = count[n]
                max_n = n
        
        return max_n
            
        