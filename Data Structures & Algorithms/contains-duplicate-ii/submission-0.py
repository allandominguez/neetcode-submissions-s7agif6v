class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = dict()

        for i, n in enumerate(nums):
            if n in indices:
                if abs(i - indices[n]) <= k:
                    return True
            indices[n] = i
        
        return False
        