class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, path, target):
            if target == 0:
                result.append(path.copy())
                return

            
            
            if i >= n or target < 0:
                return
            num = candidates[i]
            path.append(num)

            backtrack(i+1, path, target-num)
            path.pop()
            
            while  i <n-1 and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, path, target)

        backtrack(0, [], target)
        return result
        