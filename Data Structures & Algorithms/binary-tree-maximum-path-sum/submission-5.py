# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = root.val

        def getSum(node):
            if not node:
                return 0

            left = getSum(node.left)
            left = max(left, 0)

            right = getSum(node.right)
            right = max(right, 0)

            self.max = max(self.max, node.val + left + right)

            return node.val + max(left, right)

        getSum(root)
        return self.max


        