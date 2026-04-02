class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs_dict = defaultdict(list)
        for i, s in enumerate(strs):
            sorted_s = str(sorted(s))
            if sorted_s in sorted_strs_dict:
                sorted_strs_dict[sorted_s].append(i)
            else:
                sorted_strs_dict[sorted_s] = [i]
        
        result = []
        for sorted_s, index_array in sorted_strs_dict.items():
            result.append([strs[i] for i in index_array])
        
        return result
