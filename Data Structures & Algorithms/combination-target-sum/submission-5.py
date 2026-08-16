class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def backtrack(i, path, target):
            if target == 0:
                result.append(path.copy())
                return
            
            if i >= n or target < 0:
                return
            
            for j in range(i, len(nums)):
                num = nums[j]
                if target - num < 0:
                    return
                path.append(num)

                backtrack(j, path, target-num)
                path.pop()
           
        
        backtrack(0, [], target)
        return result


        