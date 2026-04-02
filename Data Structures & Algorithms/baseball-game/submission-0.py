class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                r = stack.pop()
                l = stack.pop()
                stack.extend([l, r, l + r])
            elif op == "D":
                prev = stack.pop()
                stack.extend([prev, prev * 2])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
        