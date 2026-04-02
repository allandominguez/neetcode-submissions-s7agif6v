class Solution:
    def trap(self, heights: List[int]) -> int:
        # need to iterate from left to right 
        # to find the max value for each array point
        max_left = 0
        containers = []
        for h in heights:
            # store
            containers.append([max_left])
            #compare and adjust max_left
            max_left = max(max_left, h)
        
        # need to iterate from right to left to do the same
        max_right = 0
        for i, h in enumerate(reversed(heights)):
            containers[-i - 1].append(max_right)
            max_right = max(max_right, h)
        
        # now, iterate through heights and 
        # sum += max(min(*containers[i]) - h, 0)
        water_trapped = 0
        for i, h in enumerate(heights):
            water_trapped += max(min(*containers[i]) - h, 0)
        
        return water_trapped
        