class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l = 0, r = 0;
        let max = 0;
        const currCh = new Set();
        while (r < s.length) {
            while (currCh.has(s[r])) {
                currCh.delete(s[l]);
                l++;
            }
            currCh.add(s[r]);
            max = Math.max(max, currCh.size);
            r++;
        }
        return max;
    }
}
