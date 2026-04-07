class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1
        res = 0
        for n in nums:
            cur_sum += n
            target = cur_sum - k
            res += prefix_dict[target]
            prefix_dict[cur_sum] += 1
        
        return res
