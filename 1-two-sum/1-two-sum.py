class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedMap = {}
        
        for index, num in enumerate(nums):
            val = target - num
            if val in visitedMap:
                return index, visitedMap[val]
            else:
                visitedMap[num] = index
        