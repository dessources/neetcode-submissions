# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        nodes = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                q.appendleft(node.right)
                q.appendleft(node.left)
                nodes.append(str(node.val))
            else:
                nodes.append(str(None))
        while nodes and nodes[-1] == 'None':
            nodes.pop()

        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        nodes = data.split(",") if data else []
        n = len(nodes)

        def preoder_traverse(i):
            if i >= n:
                return (None, i)
            val = nodes[i]
            i += 1
            if val != 'None':
                node = TreeNode(int(val))
                node.left, i = preoder_traverse(i)
                node.right, i = preoder_traverse(i)
                return (node, i)
            else:
                return (None, i)
        return preoder_traverse(0)[0]
