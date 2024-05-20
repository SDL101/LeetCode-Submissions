class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        counter = 0
        
        while (l >= 0 and l < r) and (r < len(nums)):
            if nums[l] + nums[r] == k:
                counter += 1
                del nums[r]
                del nums[l]
                r -= 2
            elif nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
        return counter