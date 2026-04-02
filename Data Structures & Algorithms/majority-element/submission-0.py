class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        last = 0

        for n in nums:
            if count == 0:
                last = n
            if n == last:
                count += 1
            else:
                count -= 1
        
        return last
            
        