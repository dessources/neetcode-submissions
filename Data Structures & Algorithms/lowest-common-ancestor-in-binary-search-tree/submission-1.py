# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_val = p.val
        self.q_val = q.val
        self.found = False
        hm = {}
        
        def dfs(node, val) -> Optional['TreeNode']:
            if not node:
                return None
            
            if val == node.val:
                return node
            else:
                left_result = dfs(node.left, val)
                if left_result:
                    if left_result in hm:
                        self.found = True
                    else:
                        hm[left_result] = True
                        return node
                    return left_result
                    
                right_result = dfs(node.right, val)
                if right_result:
                    if right_result in hm:
                        self.found = True
                    else:
                        hm[right_result] = True
                        return node
                    return right_result
                    
        
        p_ancestor = dfs(root, p.val)
        q_ancestor = dfs(root, q.val)
        
        return q_ancestor #type: ignore