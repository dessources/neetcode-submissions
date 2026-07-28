class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1
            num = nums[i]
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l+=1
                else:
                    cur_sum = num + nums[l] + nums[r]
                    if cur_sum == 0:
                        result.append([num, nums[l], nums[r]])
                        l+=1
                        r-=1
                    elif cur_sum > 0:
                        r -=1
                    else:
                        l+=1
        return result