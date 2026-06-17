class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for p in prices:
            profit = max(profit, p-min_price)
            min_price = min(min_price, p)
        
        return profit