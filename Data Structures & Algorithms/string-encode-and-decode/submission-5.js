class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = "";
        for (let s of strs) {
            encoded += s.length + "#" + s;
        }
        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        const decoded = [];
        let i = 0;
        while (i < str.length) {
            let j = i;
            while (str[j] !== "#") {
                j++;
            }
            let len = parseInt(str.substring(i, j));
            j += 1;
            decoded.push(str.substring(j, j + len));
            i = j + len;
        }
        return decoded;
    }
}
