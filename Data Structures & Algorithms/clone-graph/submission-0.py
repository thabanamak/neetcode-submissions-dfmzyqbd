"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}


        def dfs(u):
            if u in hashmap:
                return hashmap[u]

            copy = Node(u.val)
            hashmap[u] = copy 
            for x in u.neighbors:
                copy.neighbors.append(dfs(x))
            return copy 

        return dfs(node) if node else None
            
        