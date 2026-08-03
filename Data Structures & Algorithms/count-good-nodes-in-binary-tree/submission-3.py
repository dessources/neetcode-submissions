# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def count_good(node: TreeNode, min_val:int):
            if not node:
                return

            if node.val >= min_val:
                self.count += 1

            min_val = max(min_val, node.val)
            count_good(node.left, min_val)
            count_good(node.right, min_val )
        
        count_good(root, root.val)
        return self.count


        