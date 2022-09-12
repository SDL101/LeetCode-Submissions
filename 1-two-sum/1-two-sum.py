class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valindex_map = {}
        
        for index, num in enumerate(nums):
            value = target - num
            if value in valindex_map:
                return valindex_map[value], index
            else:
                valindex_map[num] = index
            
            