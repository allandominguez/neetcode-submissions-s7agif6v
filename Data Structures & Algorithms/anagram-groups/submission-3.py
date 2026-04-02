class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            bucket_count = [0] * 26
            for c in s:
                bucket_count[ord(c) - ord('a')] += 1
            anagrams[tuple(bucket_count)].append(s)
        
        return list(anagrams.values())
        