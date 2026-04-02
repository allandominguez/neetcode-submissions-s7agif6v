class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_i, right_i = 0, len(heights) - 1
        max_area = 0
        while left_i < right_i:
            curr_area = min(heights[left_i], heights[right_i]) * (right_i - left_i)
            if curr_area > max_area:
                max_area = curr_area
            if heights[left_i] < heights[right_i]:
                left_i += 1
            else:
                right_i -= 1
        
        return max_area
            
        