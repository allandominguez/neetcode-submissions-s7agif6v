# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._dfs(root)[0]
    
    def _dfs(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        """
        Finds if this root node is balanced, and it's height.
        """
        if root is None:
            return (True, 0)
        left, right = self._dfs(root.left), self._dfs(root.right)
        is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return (is_balanced, 1 + max(left[1], right[1]))
        