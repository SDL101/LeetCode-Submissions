class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        current = 0
        for index in range(len(nums)):
            current += nums[index]
            
            if current - nums[index] == total - current:
                return index
            
        return -1
            