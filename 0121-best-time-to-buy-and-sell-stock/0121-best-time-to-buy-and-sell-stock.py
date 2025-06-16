class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # Example Array: prices = [7, 20, 1, 100, 3, 6, 4]

       # default return - if no profit, return 0
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)
                r += 1
        
        return maxProfit

        # Time Complexity:
        # Space Complexity: