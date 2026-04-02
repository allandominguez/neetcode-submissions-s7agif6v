# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def _recursive(node: Optional[TreeNode]):
            if node is None:
                return
            
            _recursive(node.left)
            res.append(node.val)
            _recursive(node.right)
        
        _recursive(root)
        return res
        