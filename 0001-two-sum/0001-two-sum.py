class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitedIdxMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visitedIdxMap:
                return [visitedIdxMap[diff], i]
            visitedIdxMap[num] = i