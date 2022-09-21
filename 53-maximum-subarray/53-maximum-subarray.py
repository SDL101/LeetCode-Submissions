class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if len(nums) > 1 and nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
            
                