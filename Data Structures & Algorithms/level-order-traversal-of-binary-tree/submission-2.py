# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.list = []

        def buildList(node, level):
            if not node:
                return
            if len(self.list) == level:
                self.list.append([])

        
            self.list[level].append(node.val)
            buildList(node.left, level +1)
            buildList(node.right, level +1)
               
        if root:
            buildList(root, 0)
            return self.list
        return []
                
                    
                    
        