
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        seen = set()
        nodes = {i: [] for i in range(n)}
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)
        # print(nodes)

        def dfs(node, prev):

            if node in seen:
                return False

            seen.add(node)
            for neigh in nodes[node]:
                if neigh != prev and not dfs(neigh, node):
                    return False

            return True

        return dfs(0, None) and n == len(seen)