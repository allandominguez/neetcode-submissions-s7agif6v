class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> charCount = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            charCount.merge(s.charAt(i), 1, Integer::sum);
        }

        Character c;
        for (int i = 0; i < t.length(); i++) {
            c = t.charAt(i);
            if (!charCount.containsKey(c)) {
                return false;
            }
            charCount.merge(
                c, -1, (existing, decrement) -> {
                    int newValue = existing + decrement;
                    return newValue == 0 ? null : newValue;
                }
            );
        }
        
        if (charCount.isEmpty())
            return true;
        return false;
    }
}
