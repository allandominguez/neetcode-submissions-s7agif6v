class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [(0, 0, "")]	# (number of open parentheses, number of closed parentheses, current parentheses string)
        while stack:
            open_count, close_count, curr_str = stack.pop()
            if open_count == close_count == n:
                result.append(curr_str)
                continue
            if open_count < n:
                stack.append((open_count + 1, close_count, curr_str + "("))
            if close_count < open_count:
                stack.append((open_count, close_count + 1, curr_str + ")"))
        return result
