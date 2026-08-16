class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        seen = set()

        def backtrack(i,path):
            if len(path) == n:
                result.append(path.copy())
                return

            for j in range(n):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                seen.add(nums[j])
                backtrack(j, path)
                path.pop()
                seen.remove(nums[j])
               
            
        backtrack(0,[])
        return result
        