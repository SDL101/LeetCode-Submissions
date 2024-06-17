class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i <= (len(nums) - 3):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                del(nums[i])
            else:
                i += 1
        return len(nums)
                
        