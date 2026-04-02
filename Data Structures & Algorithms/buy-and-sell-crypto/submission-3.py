class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # starting from index 0 (left), we calculate the profit with a right pointer; right - left
        # if any prices[i] < left, we make left = prices[i], then iterate right again and calculate profits
        # at each step we compare profit to max_profit 
        # O(n)
        max_profit = 0
        min_price = prices[0]
        
        for p in prices[1:]:
            profit = p - min_price
            max_profit = max(max_profit, profit)

            min_price = min(min_price, p)
        
        return max_profit
        