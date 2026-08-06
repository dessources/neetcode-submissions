
class Codec:

    def serialize(self, root):
        if not root:
            return ""
        nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
            nodes.append(str(node.val) if node else "N")
        
        return ",".join(nodes)

        

    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
        self.idx = 0
        def recurse():
            if self.idx >= len(vals):
                return None
            val = vals[self.idx]
            self.idx += 1
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = recurse()
            node.right = recurse()
            return node
        
        return recurse()

        
