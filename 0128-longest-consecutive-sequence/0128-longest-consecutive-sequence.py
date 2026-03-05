class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set with nums
        # we know the max len of a sequence is the len of nums
        # iterate over nums arr and check if the value + 1 exists in set
        # while it does exist inc the maxConsecLen var by 1, else continue to next num
        # when we finish processing the nums arr, return the maxConsecLen count

        numSet = set(nums)
        maxConsecLen = 0
        if len(nums) == 0:
            return maxConsecLen
        for num in numSet:
            currConsecLen = 1
            if (num - 1) not in numSet:
                startOfSeq = num
                while (startOfSeq + 1) in numSet:
                    currConsecLen += 1
                    startOfSeq += 1
                maxConsecLen = max(currConsecLen, maxConsecLen)
        return maxConsecLen

