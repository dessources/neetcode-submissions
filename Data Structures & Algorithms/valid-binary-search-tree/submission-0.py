# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursiveIsValidBST(node, max_val, min_val) -> bool:
            if not node:
                return True
            if node.val >= max_val or node.val <= min_val:
                return False
            
            return recursiveIsValidBST(node.left, node.val, min_val) and recursiveIsValidBST(node.right, max_val, node.val)
            
        
        return recursiveIsValidBST(root, float('inf'), float('-inf'))