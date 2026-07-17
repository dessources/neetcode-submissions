# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            dl, ldl = self.longestDistance(root.left)
            dr, ldr = self.longestDistance(root.right)
            return max( max(dl, dr), ldl+ ldr)
        else: return 0
        
    def longestDistance(self, root: Optional[TreeNode]) -> Tuple[int,int]:
        if root:
            dl, ldl = self.longestDistance(root.left) 
            dr, ldr = self.longestDistance(root.right)
            d = max(max(dl, dr), ldl + ldr) 
            return d , max(ldl, ldr) + 1
        return (0,0)