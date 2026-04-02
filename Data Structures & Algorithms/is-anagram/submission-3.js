class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // confirm lengths are the same
        if (s.length != t.length) {
            return false;
        }

        // count the characters in s and t
        const sCount = {};
        const tCount = {};
        for (let i = 0; i < s.length; i++) {
            sCount[s[i]] = (sCount[s[i]] || 0) + 1;
            tCount[t[i]] = (tCount[t[i]] || 0) + 1;
        }

        // compare the counts
        for (let i = 0; i < s.length; i++) {
            if (sCount[s[i]] != tCount[s[i]]) {
                return false;
            }
        }

        return true;
    }
}
