class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # iterate for prefix sum
        prefix = [0] * len(nums)
        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            prefix[i] = cur_sum
            
        # then iterate to find target `S[j] - k`
        # would need a dict to store previous prefix sums, 
        # but only the count of sum occurrences
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        res = 0
        for p in prefix:
            res += prefix_count[p - k]
            prefix_count[p] += 1
        
        return res
