class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            

            ans = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    ans = min(ans, 1+dfs(amount-coin))
            dp[amount] = ans
            return ans
        ans = dfs(amount)
        return ans if ans < float('inf') else -1
        