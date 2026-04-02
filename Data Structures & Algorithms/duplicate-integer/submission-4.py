class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set to track visited numbers
        visited = set()
        # iterate and store the numbers
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        # otherwise, if that never happes, return False
        return False
         