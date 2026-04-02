class MyQueue:

    def __init__(self):
        self._push_stack = []
        self._reverse_stack = []

    def push(self, x: int) -> None:
        self._push_stack.append(x)

    def pop(self) -> int:
        if not self._reverse_stack:
            while self._push_stack:
                self._reverse_stack.append(self._push_stack.pop())
        return self._reverse_stack.pop()

    def peek(self) -> int:
        if not self._reverse_stack:
            while self._push_stack:
                self._reverse_stack.append(self._push_stack.pop())
        return self._reverse_stack[-1]

    def empty(self) -> bool:
        return len(self._push_stack) == 0 and len(self._reverse_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()