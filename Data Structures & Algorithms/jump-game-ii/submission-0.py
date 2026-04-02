class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = [float('inf')] * len(nums)
        queue = deque()
        queue.append((0, 0))	# (curr index, curr # of jumps)
        while queue:
            i, curr_jumps = queue.popleft()
            if i >= len(nums) or curr_jumps >= min_jumps[i]:
                continue
            min_jumps[i] = curr_jumps
            max_jump = nums[i]
            for j in range(i + 1, min(len(nums), i + max_jump + 1)):
                queue.append((j, curr_jumps + 1))
        return min_jumps[-1]

        