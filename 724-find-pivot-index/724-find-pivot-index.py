class Solution: 
    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        left_half = 0
        total = sum(nums)
        
        # nums = [1,7,3,6,5,6]
        #output 3
        
        while index < len(nums):
            if (total - left_half - nums[index]) == left_half:
                return index 
            left_half += nums[index] #1,8,11
            index += 1
            
        return -1