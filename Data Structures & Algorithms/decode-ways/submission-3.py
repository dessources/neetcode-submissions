class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[-1] = 1

        def backtrack(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0
       
            if not dp[i]:
                dp[i] = backtrack(i+1)

            if i < n-1 and (s[i] == "1" or s[i]=="2" and int(s[i+1]) in range(0,7)):
                return dp[i] + backtrack(i+2)
            return dp[i]
        
        return backtrack(0)
        # return


        