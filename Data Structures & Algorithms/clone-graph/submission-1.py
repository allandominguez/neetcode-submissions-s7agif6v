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
            # if visited, continue
            if node in visited:
                return visited[node]
            # store neighbours
            copy = Node(node.val)
            visited[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        # return new node
        return dfs(node) if node else None
