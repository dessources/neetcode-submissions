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

        def recursiveBuildTree(slice) -> Optional[TreeNode]:
            if not slice or self.count >= n:
                return None
            val = preorder[self.count]
            node = TreeNode(val)
            self.count += 1
            idx = slice.index(val)
            node.left = recursiveBuildTree(slice[:idx])
            node.right = recursiveBuildTree(slice[idx+1:])
            return node

        return recursiveBuildTree(inorder)