class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s2.length() < s1.length()) return false;
        
        int alphabet = 26;
        int[] s1Count = new int[alphabet];
        for (char c : s1.toCharArray()) {
            s1Count[c - 'a']++;
        }
        // System.out.println(Arrays.toString(s1Count));

        // todo: combine with above iteration
        int[] s2Count = new int[alphabet];
        for (int i = 0; i < s1.length(); i++) {
            s2Count[s2.charAt(i) - 'a']++;
        }
        // System.out.println(Arrays.toString(s2Count));

        int matches = 0;
        for (int i = 0; i < alphabet; i++) {
            if (s1Count[i] == s2Count[i]) matches++;
        }

        int l = 0;
        int r = s1.length();
        while (r < s2.length()) {
            // System.out.println(matches);
            if (matches == alphabet) return true;

            // todo: just track the index, not the value
            int index = s2.charAt(r) - 'a';
            s2Count[index]++;
            if (s2Count[index] == s1Count[index]) {
                matches++;
            } else if (s2Count[index] == s1Count[index] + 1) {
                matches--;
            }
            r++;

            index = s2.charAt(l) - 'a';
            s2Count[index]--;
            if (s2Count[index] == s1Count[index]) {
                matches++;
            } else if (s2Count[index] == s1Count[index] - 1){
                matches--;
            }
            l++;
        }
        return matches == alphabet;
    }
}
