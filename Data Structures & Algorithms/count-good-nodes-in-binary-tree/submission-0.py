# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def recursiveGoodNodes(node, max_val) -> int:
            if not node:
                return 0
            count = 0 if node.val < max_val else 1
            max_val = max(max_val, node.val)
            return count + recursiveGoodNodes(node.left,max_val) + recursiveGoodNodes(node.right,max_val)
        
        max_val = root.val
        return 1 + recursiveGoodNodes(root.left,max_val) + recursiveGoodNodes(root.right,max_val)
        