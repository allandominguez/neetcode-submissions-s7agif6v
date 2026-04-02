class Solution:
    def isNStraightHand(self, hand: List[int], group_size: int) -> bool:
        if len(hand) % group_size != 0:
            return False
        num_of_hands = int(len(hand) / group_size)
        num_count = defaultdict(int)
        minimum = float('inf')
        for n in hand:
            num_count[n] += 1
            minimum = min(n, minimum)
        for _ in range(num_of_hands):
            curr = minimum
            for _ in range(group_size):
                if curr not in num_count:
                    return False
                num_count[curr] -= 1
                if num_count[curr] == 0:
                    num_count.pop(curr)
                    minimum = curr + 1
                curr += 1
            if num_count and minimum not in num_count:
                minimum = min(num_count.keys())
        return True
