class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = ''.join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(stripped_s) - 1

        while left < right:
            if stripped_s[left] != stripped_s[right]:
                return False
            left += 1
            right -= 1

        return True
