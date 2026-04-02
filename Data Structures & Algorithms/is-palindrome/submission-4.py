class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer; left to right, right to left
        # we need to move the pointer until it finds an alpha-character
        # and also convert to lower case
        # exit early if we find a mismatch
        # exit loop once left >= right; this means it is a valid palindrome
        # e.g. "Was it a car or a cat I saw?"
        left, right = 0, len(s) - 1
        while (left < right):
            while (not s[left].isalnum() and left < right):
                left += 1
            while (not s[right].isalnum() and right > left):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
        