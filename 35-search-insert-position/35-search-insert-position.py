class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #nums = [1,2,3,4,5,6]
        #target = 2
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

        