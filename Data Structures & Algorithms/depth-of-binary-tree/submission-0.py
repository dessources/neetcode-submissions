# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count (self, node, count) -> int:
        if not node:
            return 0

        left_count = self.count(node.left, count)
        right_count = self.count(node.right, count)

        return max(left_count, right_count) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.count(root, 1)
        