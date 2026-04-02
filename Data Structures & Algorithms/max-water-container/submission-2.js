class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0, r = heights.length - 1;
        let max = 0;
        while (l < r) {
            // calculate the amount
            let width = r - l;
            let height = Math.min(heights[l], heights[r]);
            max = Math.max(max, (width * height));

            // shift whichever height is shorter
            if (heights[l] > heights[r]) {
                r--;
            } else {
                l++;
            }
        }
        return max;
    }
}
