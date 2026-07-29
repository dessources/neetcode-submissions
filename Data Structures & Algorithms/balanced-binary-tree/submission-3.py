# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def getDepth(node)->int:
            if not node:
                return 0
            
            left = getDepth(node.left)
            if not self.isBalanced:
                return 0

            right = getDepth(node.right)
            if not self.isBalanced:
                return 0
            
            if abs(left - right) > 1:
                self.isBalanced = False
            return 1+ max(left, right)
        getDepth(root)
        return self.isBalanced


        