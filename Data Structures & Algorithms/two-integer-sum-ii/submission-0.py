class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front_ind = 0
        end_ind = len(numbers) - 1

        while front_ind <= end_ind:
            curr_sum = numbers[front_ind] + numbers[end_ind]
            if curr_sum < target:
                front_ind += 1
            elif curr_sum > target:
                end_ind -= 1
            else:
                return [front_ind + 1, end_ind + 1]
        return []
        