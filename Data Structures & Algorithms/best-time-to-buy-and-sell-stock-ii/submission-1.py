class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, p in enumerate(prices[1:]):
            if prices[i] < p:
                profit += p - prices[i]
        return profit
        