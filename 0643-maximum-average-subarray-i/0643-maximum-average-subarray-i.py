class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #setup the maxSum and currSum with sum of the first k elements
        maxSum = sum(nums[:k])
        currSum = maxSum
        
        for i in range(k, len(nums)):
            # add new element on right, delete old element on left
            currSum += nums[i]
            currSum -= nums[i - k]
            
            # if new sum is larger, store it in maxSum
            maxSum = max(maxSum, currSum)
            
        # return maxSum divided by the num of elements
        return (maxSum / k)
            
            