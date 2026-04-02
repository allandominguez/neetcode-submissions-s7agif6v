class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const chCount = new Map();
        let maxFreq = 0;
        let maxLength = 0;
        let l = 0, r = 0;
        while (r < s.length) {
            chCount[s[r]] = (chCount[s[r]] || 0) + 1;
            maxFreq = Math.max(maxFreq, chCount[s[r]]);
            if ((r - l + 1) - maxFreq > k) {
                chCount[s[l]]--;
                l++;
            }
            maxLength = Math.max(maxLength, (r - l + 1));
            r++;
        }
        return maxLength;
    }
}
