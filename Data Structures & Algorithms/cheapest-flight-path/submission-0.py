class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_map = defaultdict(list)
        for start, end, price in flights:
            flight_map[start].append((end, price))
        queue = deque()
        for end, price in flight_map[src]:
            queue.append((end, price, 0))
        best_price = float('inf')
        while queue:
            ap, curr_price, num_flights = queue.popleft()
            if num_flights > k:
                continue
            if ap == dst and curr_price < best_price:
                best_price = curr_price
                continue
            for next_ap, next_price in flight_map[ap]:
                queue.append((next_ap, curr_price + next_price, num_flights + 1))
        return -1 if best_price == float('inf') else best_price
        