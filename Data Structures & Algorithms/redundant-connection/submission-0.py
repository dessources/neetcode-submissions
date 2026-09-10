class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

 
        def find(v):
            if v != par[v]:
                par[v] = find(par[v])
            return par[v]

        def union(v1, v2):
            v1, v2 = find(v1), find(v2)
            if v1 == v2:
                return False
        
            if rank[v1] > rank[v2]:
                par[v2] = v1
                rank[v1] += rank[v2]
            else:
                par[v1] = v2
                rank[v2] += rank[v1]
       
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]

        
        

        
     

