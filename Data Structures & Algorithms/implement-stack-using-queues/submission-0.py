class MyStack:

    def __init__(self):
        self._a = deque([])
        self._b = deque([])
    
    def _get_current_queue(self) -> deque:
        if self._a:
            return self._a, self._b
        return self._b, self._a

    def push(self, x: int) -> None:
        curr, _ = self._get_current_queue()
        curr.append(x)

    def pop(self) -> int:
        curr, empty = self._get_current_queue()
        while len(curr) > 1:
            empty.append(curr.popleft())
        return curr.popleft()

    def top(self) -> int:
        curr, empty = self._get_current_queue()
        while len(curr) > 1:
            empty.append(curr.popleft())
        res = curr.popleft()
        empty.append(res)
        return res

    def empty(self) -> bool:
        curr, _ = self._get_current_queue()
        return len(curr) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()