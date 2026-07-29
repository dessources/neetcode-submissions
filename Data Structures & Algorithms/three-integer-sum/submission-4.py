class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i,num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i-1] == num:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l+=1
                else:
                    cur_sum = num + nums[l] + nums[r]
                    if not cur_sum:
                        result.append([num, nums[l], nums[r]])
                        l+=1
                        r-=1
                    elif cur_sum > 0:
                        r -=1
                    else:
                        l+=1
        return result
            

        