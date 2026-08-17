class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(s, i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

        n = len(s)
        result = []
        partition = []

        def backtrack(i):
            if i >= n:
                result.append(partition.copy())
                return
            
            for j in range(i, n):
                if not isPali(s, i, j):
                    continue
                partition.append(s[i:j+1])
                backtrack(j+1)
                partition.pop()
        
        backtrack(0)
        return result

            
        