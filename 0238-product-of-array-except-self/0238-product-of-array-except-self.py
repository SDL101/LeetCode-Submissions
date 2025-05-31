class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPass, rightPass = [1] * len(nums), [1] * len(nums)
        prod = 1
        for i in range(1, len(nums)):
            leftPass[i] = leftPass[i-1] * nums[i-1] 
            
        for i in range(len(nums)-2, -1, -1):
            prod = prod * nums[i+1]
            rightPass[i] = prod
        
        for i in range(len(nums)):
            leftPass[i] = leftPass[i] * rightPass[i]
        return leftPass 
