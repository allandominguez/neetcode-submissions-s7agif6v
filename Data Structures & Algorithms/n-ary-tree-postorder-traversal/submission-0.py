"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def postorder(root):
            if root is None:
                return
            
            # iterate through children to process through postorder()
            for node in root.children:
                postorder(node)

            # then, append the current value
            res.append(root.val)
        
        postorder(root)
        return res
        