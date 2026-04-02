class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (length * 2)
        for i, n in enumerate(nums):
            ans[i] = n
            ans[length + i] = n
        return ans
        