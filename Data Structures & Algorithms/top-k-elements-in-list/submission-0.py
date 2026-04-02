class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ordered_frequency = [set() for _ in nums]
        num_index = {}

        for num in nums:
            if num not in num_index:
                ordered_frequency[0].add(num)
                num_index[num] = 0
            else:
                ordered_frequency[num_index[num]].remove(num)
                num_index[num] += 1
                ordered_frequency[num_index[num]].add(num)
        
        result = []
        for group in reversed(ordered_frequency):
            result.extend(group)
            if len(result) >= k:
                return result[:k]
        
        return []
        