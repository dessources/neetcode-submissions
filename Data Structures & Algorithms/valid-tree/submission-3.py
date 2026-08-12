class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True

        hm = {i:[] for i in range(n)}

        seen = set()
        checked = [False]*n

        for  a,b in edges:
            hm[a].append(b)
            hm[b].append(a)
            
        print(hm)
        def dfs(node, parent):
            if node in seen:
                return False
            
            seen.add(node)
            if node in hm:
                for neigh in hm[node]:
                    if neigh != parent and not dfs(neigh,node):
                        return False
            return True

        components = 0
        for node in hm:
            if node not in seen:
                if components > 0:
                    return False
                if not dfs(node, None):
                    return False
            components+=1
            

        return True