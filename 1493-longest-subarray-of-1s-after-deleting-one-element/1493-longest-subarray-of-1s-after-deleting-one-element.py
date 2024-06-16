class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # elif len(nums) == sum(nums):
        #     return len(nums) - 1
        # else:
        left = 0
        k = 1

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left