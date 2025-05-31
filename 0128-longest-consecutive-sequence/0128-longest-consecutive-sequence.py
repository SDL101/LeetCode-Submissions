class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        maxLen = 1
        for num in numSet:
            if num - 1 not in numSet:
                start = num
                currLen = 1
                while start + 1 in numSet:
                    currLen += 1
                    start += 1
                if currLen > maxLen:
                    maxLen = currLen
        return maxLen
            