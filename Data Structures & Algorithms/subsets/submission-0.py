class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        n = len(nums)
        nums.sort()
        def backtrack(i, path):
     
            num = nums[i]
        
            path.append(num)
            for j in range(i+1, n):
                backtrack(j, path)
            result.append(path.copy())
            path.pop()
          
        for i in range(len(nums)):
            backtrack(i, [])
        return result
        