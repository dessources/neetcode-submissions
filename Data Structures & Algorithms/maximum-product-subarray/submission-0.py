class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1,1
        ans = nums[0]

        for n in nums:
            # if n == 0:
            #     cur_min = cur_max = 1
            #     continue
            
            tmp = cur_max * n
            cur_max = max(tmp, cur_min*n, n)
            cur_min = min(tmp, cur_min*n, n)
            ans = max(ans, cur_max)
        
        return ans
        