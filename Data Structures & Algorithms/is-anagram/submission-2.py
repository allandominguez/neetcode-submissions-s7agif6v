class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary of key: char, val: count
        # iterate and count the characters in s
        char_count = dict()
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        # iterate t and decrement and remove the characters from the dictionary
        # return False if any character is not in the dictionary
        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] == 0:
                char_count.pop(c)
        
        # return if the dictionary is empty or not
        return len(char_count) == 0
        