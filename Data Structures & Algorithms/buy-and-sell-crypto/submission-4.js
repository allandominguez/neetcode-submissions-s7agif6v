class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let l = 0, r = 0;
        let max = 0;
        while (r < prices.length) {
            max = Math.max(max, (prices[r] - prices[l]));
            if (prices[r] < prices[l]) {
                l = r;
            }
            r++;
        }
        return max;
    }
}
