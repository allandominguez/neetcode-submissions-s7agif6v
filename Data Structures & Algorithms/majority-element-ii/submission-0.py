class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

            if len(count) > 2:
                # decrement and remove
                new_count = defaultdict(int)
                for n, c in count.items():
                    if c > 1:
                        new_count[n] = c - 1
                count = new_count
            
        candidates = { c: 0 for c in count.keys() }
        for n in nums:
            if n in candidates:
                candidates[n] += 1
        
        return [n for n in candidates.keys() if candidates[n] > (len(nums) // 3)]
        