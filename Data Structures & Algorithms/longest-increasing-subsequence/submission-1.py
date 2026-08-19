class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        done = [False] *n
        max_len = 1
        def backtrack(i):
            if i >= n:
                return 0
            if done[i]:
                return dp[i]

            for j in range(i+1,n):
                if nums[i] >= nums[j]:
                    continue
                dp[i] = max(dp[i], 1+ backtrack(j))
            
            done[i] = True
            return dp[i]
        
        for i in range(n):
            max_len = max(max_len, backtrack(i))
        print(dp)
        return max_len
        