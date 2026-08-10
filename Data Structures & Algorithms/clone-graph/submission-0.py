"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = set()
        copy_nodes = {}

        def dfs(node):
            seen.add(node.val)
            copy_node = Node(node.val)
            copy_nodes[copy_node.val] = copy_node

            for n in node.neighbors:
                if n.val not in seen:
                    seen.add(n.val)
                    copy_node.neighbors.append(dfs(n))
                else:
                    copy_node.neighbors.append(copy_nodes[n.val])
            

            return copy_node

        return dfs(node) if node else None