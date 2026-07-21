# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.count = 0
        n = len(preorder)

        def recursiveBuildTree(l, r) -> Optional[TreeNode]:
            if l >= r or self.count >= n:
                return None
            val = preorder[self.count]
            node = TreeNode(val)
            self.count += 1
            idx = inorder.index(val)
            node.left = recursiveBuildTree(l, idx)
            node.right = recursiveBuildTree(idx+1, r)
            return node

        return recursiveBuildTree(0, n)