class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        res = [0 for _ in range(len(nums))]
        res[0] = 1

        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]

        rp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rp
            rp *= nums[i]

        return res
       
