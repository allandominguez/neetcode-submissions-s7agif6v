# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self._diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)
        return self._diameter

    def _dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self._dfs(root.left)
        right = self._dfs(root.right)

        self._diameter = max(self._diameter, left + right)

        return 1 + max(left, right)
