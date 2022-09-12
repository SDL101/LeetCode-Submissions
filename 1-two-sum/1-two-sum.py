class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIndexMap = {}
        
        for index, num in enumerate(nums):
            value = target - num
            if value in valIndexMap:
                return valIndexMap[value], index
            else:
                valIndexMap[num] = index 
                