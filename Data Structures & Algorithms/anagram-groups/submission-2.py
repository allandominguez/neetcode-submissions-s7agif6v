class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            ch_count = [0] * 26
            for ch in s:
                ch_count[ord(ch) - ord('a')] += 1
            anagram_dict[tuple(ch_count)].append(s)
        return [anagram_list for _, anagram_list in anagram_dict.items()]