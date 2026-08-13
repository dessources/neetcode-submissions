
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        hm = {i:[] for i in range(n)}

        seen = set()


        for  a,b in edges:
            hm[a].append(b)
            hm[b].append(a)
        
       
        def dfs(node, parent):
       
            if node in seen:
                return False
            
            seen.add(node)
            if node in hm:
                for neigh in hm[node]:
                    if neigh != parent and not dfs(neigh,node):
                        return False
          
            return True

        return dfs(0, None) and n == len(seen)