class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # slide the window, incrementing/decrementing the 
        # min_count as per 'W' occurrence and removal
        # keeping track of the min_count of 'W' only when 
        # window is of size k
        l = r = 0
        min_count, w_count = len(blocks), 0

        while r < len(blocks):
            if blocks[r] == 'W':
                w_count += 1
            if r - l == k - 1:
                min_count = min(min_count, w_count)
                if blocks[l] == 'W':
                    w_count -= 1
                l += 1
            r += 1
        
        return min_count
        