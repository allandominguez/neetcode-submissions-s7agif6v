class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = dict()
        for c in s:
            if c in char_count:
                char_count[c] = char_count[c] + 1
            else:
                char_count[c] = 1
        
        for c in t:
            if c in char_count:
                char_count[c] = char_count[c] - 1
                if char_count[c] == 0:
                    char_count.pop(c)
            else:
                return False
        
        if char_count:
            return False
        return True