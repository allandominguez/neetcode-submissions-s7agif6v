"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:       
        # keep track of visited nodes; dict
        visited = dict()

        # dfs recursion (takes a Node) -> expects the Node copy:
        def dfs(n: 'Node') -> 'Node':
            # if we've visited the node, return the node copy
            if n in visited:
                return visited[n]

            # otherwise
            # create a new node and copy the val
            n_copy = Node(n.val)
            # store node in visited; {og node: node}
            visited[n] = n_copy

            # then iterate and copy the neighbours recursively
            for neighbor in n.neighbors:
                n_copy.neighbors.append(dfs(neighbor))

            # return node copy
            return n_copy
        
        return dfs(node) if node else None
