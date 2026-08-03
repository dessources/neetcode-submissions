class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [0]*(n+1)
        self.dp[0] = 1

        def recurse(n) -> int:
            if n < 0:
                return 0
            
            if not self.dp[n]:
                self.dp[n] = recurse(n-2) + recurse(n-1)
                
            return self.dp[n]
        
        return recurse(n)

        