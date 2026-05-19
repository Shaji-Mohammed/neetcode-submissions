"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        newToOld = {}

        def dfs(node):
            if node in newToOld:
                return newToOld[node]

            clone = Node(node.val)
            newToOld[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        
        return dfs(node)
        
                
