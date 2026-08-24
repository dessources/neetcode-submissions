class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        # dp[-1] = 1

        def backtrack(i):
            if i >= n:
                return 1
            if s[i] == '0':
                return 0

            if dp[i] == -1:
                dp[i]= backtrack(i+1)
                if i+1 < n and (s[i] == '1' or s[i]=='2' and s[i+1] in "0123456"):
                    dp[i] += backtrack(i+2)
            
            return dp[i]
        
        return backtrack(0)


        
        


        