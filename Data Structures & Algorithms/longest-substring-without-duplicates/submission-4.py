class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        left, right = 0, 1
        unique_chars = set(s[left])
        longest = 1

        while left < right < len(s):
            if s[right] in unique_chars:
                while s[right] in unique_chars:
                    unique_chars.remove(s[left])
                    left += 1
                unique_chars.add(s[right])
                right += 1
            else:
                unique_chars.add(s[right])
                longest = max(longest, len(unique_chars))
                right += 1
        
        return longest
        