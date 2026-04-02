class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = last = prices[0]
        for p in prices[1:]:
            if p < last:
                profit += last - buy
                buy = p
            last = p
        return profit + (last - buy)
        