# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def recursiveKthSmallest(node) -> Tuple[int, bool]:
            if not node:
                return (0, False)

            val, found = recursiveKthSmallest(node.left)
            if found:
                return (val, True)

            self.count += 1
            if self.count == k:
                return (node.val, True)

            return recursiveKthSmallest(node.right)

        return recursiveKthSmallest(root)[0]
        