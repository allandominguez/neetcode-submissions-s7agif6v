class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0

        for p in prices:
            max_profit = max(max_profit, p - low)
            low = min(low, p)
        
        return max_profit
        