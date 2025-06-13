class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set to store all the numbers
        numSet = set(nums)
        # iterate over the nums array and if it's not the start of a sequence (i.e. num - 1 is in set)
        # then skip over it and proceed to start counting upward in loop only when at the start of a sequence
        # [100, 4, 200, 1, 3, 2]

        maxCount = 0
        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                while (num + 1) in numSet:
                    count += 1
                    num += 1
                maxCount = max(maxCount, count)
        return maxCount

       

