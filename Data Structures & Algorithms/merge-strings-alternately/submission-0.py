class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        cur1, cur2 = 0, 0
        while (cur1 < len(word1)) and (cur2 < len(word2)):
            merged += word1[cur1] + word2[cur2]
            cur1 += 1
            cur2 += 1
        
        if cur1 < len(word1):
            merged += word1[cur1:]
        if cur2 < len(word2):
            merged += word2[cur2:]
        
        return merged

        