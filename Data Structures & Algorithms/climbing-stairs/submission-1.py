class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1: return 0
        if n < 2: return 1
        curr,prev = 2,1
        for i in range(2,n):
            curr, prev = curr+prev, curr
        return curr
