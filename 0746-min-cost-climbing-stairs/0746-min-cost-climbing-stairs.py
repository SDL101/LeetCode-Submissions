class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stepMinCost = [0 for _ in range(len(cost)+1)]
        for i in range(len(stepMinCost)):
            if i == 0 or i == 1:
                stepMinCost[i] = 0
            else:
                stepMinCost[i] = min(stepMinCost[i-1] + cost[i-1], stepMinCost[i-2] + cost[i-2])
        return stepMinCost[-1]