class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # gather the first k substring
        # calculate it's w_count of W's
        r = 0
        w_count = 0
        while r < len(blocks) and r < k:
            if blocks[r] == 'W':
                w_count += 1
            r += 1

        # get the l and r pointers of the above window
        # perform sliding window keeping track of the
        # minimum w_count
        l = 0
        min_count = w_count
        while r < len(blocks):
            if blocks[r] == 'W':
                w_count += 1
            if blocks[l] == 'W':
                w_count -= 1
            min_count = min(min_count, w_count)
            r += 1
            l += 1
        
        return min_count
        