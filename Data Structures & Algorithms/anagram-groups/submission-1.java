class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> strMap = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            String sCount = Arrays.toString(count);
            strMap.putIfAbsent(sCount, new ArrayList<String>());
            strMap.get(sCount).add(s);
        }
        return new ArrayList<>(strMap.values());
    }
}
