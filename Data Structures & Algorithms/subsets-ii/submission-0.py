class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        seen  = set()
        nums.sort()
        def backtrack(i, path):
        
            if tuple(path) not in result:
                result.add(tuple(path))
            
            if i >= n:
                return
            
            for j in range(i,n):
                # if nums[j] == nums[j-1]:
                #     continue
                num = nums[j]
                path.append(num)
                backtrack(j+1, path)
                path.pop()
            
        backtrack(0, [])
        return [list(s) for s in result]
        