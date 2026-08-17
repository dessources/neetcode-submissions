

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one_step, two_step = 0,0
        for i in range(n-1, -1, -1):
            total_cost = min(cost[i]+one_step, cost[i]+  two_step)
            one_step, two_step = total_cost, one_step
        return min(one_step, two_step)


        