class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #create a smalles and largest heap
        #since we can perform 3 swaps, the 3 smallest and 3 largest
        #would be swapped, meaning the 4th smallest/largest difference
        #is what we would return
        
        if len(nums) <= 4:
            return 0
          
        FourSmallest = sorted(heapq.nsmallest(4, nums))
        FourLargest = sorted(heapq.nlargest(4, nums))
        
        print(FourSmallest, "\n", FourLargest)
        
        minDiff = float('inf')
        for i in range(4):
            if (FourLargest[i] - FourSmallest[i]) < minDiff:
                minDiff = FourLargest[i] - FourSmallest[i]
        return minDiff
    