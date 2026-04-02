# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def _is_same(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if root is None and sub_root is None:
            return True
        if root and sub_root and root.val == sub_root.val:
            return self._is_same(root.left, sub_root.left) and self._is_same(root.right, sub_root.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if sub_root is None:
            return True
        if root is None:
            return False
        if root.val == sub_root.val:
            if self._is_same(root, sub_root):
                return True
        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)
        