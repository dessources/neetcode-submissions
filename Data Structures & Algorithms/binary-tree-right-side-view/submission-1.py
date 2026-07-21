# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            q = deque([root])
            result = []
            
            while q:
                level = []
                qLen = len(q)
                if qLen:
                    result.append(q[-1].val)
                for i in range(qLen):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            return result
        return []