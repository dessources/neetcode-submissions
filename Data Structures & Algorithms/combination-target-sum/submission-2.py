class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
      
        def recurse(start, new_target)->List[List[int]]:
            results = []
            for i in range(start, len(nums)):
                num = nums[i]
                if num > new_target:
                    break

                factor = 0
                if new_target % num == 0:
                    factor = new_target // num
                    results.append([num] * factor)
                
                for j in range(1, new_target//num):
                    if j == factor:
                        continue

                    tentative_target = new_target - (j*num)
                    if tentative_target > 0:
                        other_results = recurse(i+1,tentative_target)
                        for l in other_results:
                            l.extend([num]*j)
                        results.extend(other_results)
                    else:break
                    
            return results
        
        ans = recurse(0, target)
        return ans