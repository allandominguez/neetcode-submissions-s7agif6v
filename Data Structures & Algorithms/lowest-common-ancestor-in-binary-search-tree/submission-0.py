# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_cur = root
        q_cur = root
        p_set = set([root.val])
        q_stack = [root]
        while p_cur.val != p.val and q_cur.val != q.val:
            if p.val < p_cur.val:
                p_cur = p_cur.left
                p_set.add(p_cur.val)
            elif p.val > p_cur.val:
                p_cur = p_cur.right
                p_set.add(p_cur.val)
            
            if q.val < q_cur.val:
                q_cur = q_cur.left
                q_stack.append(q_cur)
            elif q.val > q_cur.val:
                q_cur = q_cur.right
                q_stack.append(q_cur)
        while q_stack[-1].val not in p_set:
            q_stack.pop()
        return q_stack[-1]
        