class Solution {
    /**
     * @param {char} c
     * @return {boolean}
     */
    isAlphanumeric(c) {
        return (
            (c >= 'a' && c <= 'z') ||
            (c >= 'A' && c <= 'z') ||
            (c >= '0' && c <= '9')
        )
    }

    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0;
        let r = s.length - 1;
        while (l < r) {
            while (!this.isAlphanumeric(s.charAt(l)) && l < r) {
                l++;
            }
            while (!this.isAlphanumeric(s.charAt(r)) && l < r) {
                r--;
            }
            if (s.charAt(l).toLowerCase() !== s.charAt(r).toLowerCase()) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
