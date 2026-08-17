class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = cost.copy()
        n = len(cost)
        for i in range(len(cost)-1, -1, -1):
            a = b = 0
            if i+1 < n:
                a = total_cost[i+1]
            if i+2 < n:
                b = total_cost[i+2]
            total_cost[i] = min(cost[i]+a, cost[i]+ b)
        return min(total_cost[0], total_cost[1])


        