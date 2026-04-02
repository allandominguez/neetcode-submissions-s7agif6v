class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap of numbers to indexes; {n: i}
        nums_ind = dict()
        for i, n in enumerate(nums):
            nums_ind[n] = i
        # iterate through nums:
            # subtract each num from the target
            # check if the remained is in the hashmap
            # but ensure the index isn't the current index
        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in nums_ind and nums_ind[remainder] != i:
                return [i, nums_ind[remainder]]
        return [0,0]
        