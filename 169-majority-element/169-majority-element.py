class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        half = len(nums) // 2
        
        if len(nums) == 1:
            return nums[0]
        
        for num in nums:
            if num in countMap:
                countMap[num] += 1
                if countMap[num] > half:
                    return num
            else:
                countMap[num] = 1
            
        