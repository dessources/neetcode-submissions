class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a,b = 0,0
        for i in range(len(cost)-1, -1, -1):
            total_cost = min(cost[i]+a, cost[i]+ b)
            a,b = total_cost, a
        return min(a,b)


        