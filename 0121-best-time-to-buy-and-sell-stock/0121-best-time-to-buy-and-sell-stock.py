class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit