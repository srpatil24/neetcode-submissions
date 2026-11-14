class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # maxProf = 0
        # for r in range(1, len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     maxProf = max(maxProf, prices[r]-prices[l])
        # return maxProf
        low = prices[0]
        maxProf = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
                continue
            maxProf = max(maxProf, prices[i]-low)
        return maxProf