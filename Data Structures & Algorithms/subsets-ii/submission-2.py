class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def backtrack(i, path):
            result.append(path.copy())
            
            if i >= n:
                return
            
            for j in range(i,n):
                if j>i and nums[j] == nums[j-1]:
                    continue
                num = nums[j]
                path.append(num)
                backtrack(j+1, path)
                path.pop()
            
        backtrack(0, [])
        return result
        