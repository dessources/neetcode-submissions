# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compareNodes(p,q)-> bool:
            if (not p) ^ (not q):
                return False
            
            if p and q:
                if p.val != q.val:
                    return False

                if not compareNodes(p.left, q.left):
                    return False

                if not compareNodes(p.right, q.right):
                    return False
            return True

        return compareNodes(p,q)

        