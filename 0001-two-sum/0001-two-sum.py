class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iMap = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if (target - num) in iMap:
                return [i, iMap[target - num]]
            iMap[num] = i