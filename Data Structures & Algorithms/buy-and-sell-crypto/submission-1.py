class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = high = prices[0]
        max_profit = 0

        for p in prices[1:]:
            if p < low:
                low = p
                high = p
            if p > high:
                high = p
            curr_profit = high - low
            if curr_profit > max_profit:
                max_profit = curr_profit
        
        return max_profit
        