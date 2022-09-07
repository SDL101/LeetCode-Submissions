class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #loop through the array prices
        #2 pointers - l starts at 0, r starts at 1
        #check the difference between r and l 
        #if the diff is greater than the max profit
        #update the max profit and move the right pointer
        #when right pointer reaches the end of the array
        #move the left pointer to the right one index
        #move the right pointer to one index position to the right of left
        
#         l, r = 0, 1
#         max_prof = 0
#         # for each in range(len(prices)):
#         while r < len(prices):
#             profit = prices[r] - prices[l]
#             max_prof = max(max_prof, profit)
#             r += 1
#         l += 1
#         r = l + 1

#         return max_prof

        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
    
