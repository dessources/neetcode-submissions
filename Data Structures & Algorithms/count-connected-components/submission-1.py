class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hm = {i: [] for i in range(n)}
        seen = set()

        for item in edges:
            course, prereq = item[0], item[1]
            hm[prereq].append(course)
            hm[course].append(prereq)
           
        def dfs(prereq):
            if prereq in seen:
                return
        
            seen.add(prereq)
            if prereq in hm:
                for course in hm[prereq]:
                    dfs(course)

        count  = 0
        for prereq in hm:
            if prereq not in seen:
                dfs(prereq)
                count+=1

        return count
                