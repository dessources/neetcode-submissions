class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, path, target):
            if target == 0:
                result.append(path.copy())
                return
            if target < 0:
                return

            for j in range(i,n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                backtrack(j+1, path, target-candidates[j])
                path.pop()


        backtrack(0, [], target)
        return result
        