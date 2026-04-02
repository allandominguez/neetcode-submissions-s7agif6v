class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for t in tokens:
            if t.isnumeric():
                numbers.append(int(t))
            elif (len(t) > 1) and t.startswith("-") and t[1:].isnumeric():
                numbers.append(-int(t[1:]))
            else:
                right = numbers.pop()
                left = numbers.pop()
                if t == "+":
                    result = left + right
                elif t == "-":
                    result = left - right
                elif t == "*":
                    result = left * right
                else:
                    result = int(left / right)
                numbers.append(result)
        return numbers[0]
        