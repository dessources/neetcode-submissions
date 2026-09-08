class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        seen = set()
        path = set()
        res = []

        for c, p in prerequisites:
            nodes[c].append(p)

        def traverse(i):
            if i in seen:
                return False
            if i in path:
                return True

            seen.add(i)
            for j in nodes[i]:
                if not traverse(j):
                    return []

            path.add(i)
            res.append(i)
            seen.remove(i)
            return True

        for node in range(numCourses):
            if not traverse(node):
                return []
                
        return res