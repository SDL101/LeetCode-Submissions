from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = defaultdict(int)
        for i, num in enumerate(nums):
            if (target - num) in numMap.keys():
                return [i, numMap[target-num]]
            numMap[num] = i