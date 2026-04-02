class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(f"test: {nums}")
        triplets = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            
            front_ind, end_ind = i + 1, len(nums) - 1
            while front_ind < end_ind:
                if nums[front_ind] + nums[end_ind] + num > 0:
                    end_ind -= 1
                elif nums[front_ind] + nums[end_ind] + num < 0:
                    front_ind += 1
                else:
                    triplets.append([nums[front_ind], num, nums[end_ind]])
                    front_ind += 1
                    end_ind -= 1
                    while front_ind < end_ind and nums[front_ind] == nums[front_ind - 1]:
                        front_ind += 1

        return triplets
        