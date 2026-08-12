
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        hm = defaultdict(set)
        seen = set()
        checked = [False]*numCourses

        for item in prerequisites:
            course, prereq = item[0], item[1]
            hm[course].add(prereq)

        # @cache
        def dfs(course):
            if course in seen:
                return False
            if checked[course]:
                return True

            seen.add(course)
            if course in hm:
                for prereq in hm[course]:
                    if not dfs(prereq):
                        return False
            seen.remove(course)
            checked[course] = True
            return True

        for course in hm:
            if not dfs(course):
                return False

        return True