class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        comparisonSet = set()
        for num in nums:
            if num in comparisonSet:
                return True
            else:
                comparisonSet.add(num)
        return False