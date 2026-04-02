# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []
        while queue:
            right_most = None
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                if node:
                    right_most = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_most:
                result.append(right_most.val)
        return result