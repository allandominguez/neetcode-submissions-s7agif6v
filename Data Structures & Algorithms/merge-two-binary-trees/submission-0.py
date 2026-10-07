# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # dfs(node1, node2):
        def dfs(node1, node2):
            # if node1 is None:
            if node1 is None:
                # return node2 
                return node2
            # if node2 is None:
            if node2 is None:
                # return node1 copy
                return node1
            
            # else, we return sum of node1 and node2
            new_node = TreeNode(sum((node1.val, node2.val)))
            # and process children
            new_node.left = dfs(node1.left, node2.left)
            new_node.right = dfs(node1.right, node2.right)
            return new_node
        
        return dfs(root1, root2)
        