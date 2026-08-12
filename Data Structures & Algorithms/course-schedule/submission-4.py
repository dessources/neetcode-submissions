from functools import cache
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        hm = defaultdict(set)
        seen = set()

        for item in prerequisites:
            course, prereq = item[0], item[1]
            hm[course].add(prereq)

        @cache
        def dfs(course):
            if course in seen:
                return False

            seen.add(course)
            if course in hm:
                for prereq in hm[course]:
                    if not dfs(prereq):
                        return False
            seen.remove(course)
            return True

        for course in hm:
            if not dfs(course):
                return False

        return True
            
        