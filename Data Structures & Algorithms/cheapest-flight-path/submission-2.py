class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford approach
        # we want to store the cheapest prices for reaching each airport
        # for every k stops
        # so we will need to iterate flights k + 1 times as we will
        # be updating the prices array each iteration
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            last_prices = prices.copy()
            for a, b, price in flights:
                if (last_prices[a] + price) < prices[b]:
                    prices[b] = last_prices[a] + price
        return -1 if prices[dst] == float('inf') else prices[dst]
        