"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:       
        # track visited nodes/values
        visited = dict()

        # iterate graph via DFS recursion
        def dfs(node):
            if node is None:
                return
            # if visited, continue
            if node.val in visited:
                return visited[node.val]
            # store neighbours
            copy = Node(node.val)
            visited[node.val] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        # return new node
        return dfs(node)
