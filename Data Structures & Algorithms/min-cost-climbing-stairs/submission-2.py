class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        curr,prev=0,0
        for i in range(2,n+1):
            curr,prev = min(cost[i-1]+curr, cost[i-2]+prev), curr
        return curr