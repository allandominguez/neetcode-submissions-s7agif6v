# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if both are null, return null
        if root1 is None and root2 is None:
            return None

        # we check if either is null
        # if one is, we copy over the other; i.e. return the other
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        # otherwise, return a new node with the val of the sum of the 2 nodes val
        node = TreeNode(val=root1.val + root2.val)
        
        # then process the children recursively
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        
        # return the node at the end
        return node
        