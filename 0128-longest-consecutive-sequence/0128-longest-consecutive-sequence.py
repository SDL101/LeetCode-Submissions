class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # Convert nums to a set for O(1) lookups and to handle duplicates automatically
    # Only start a new sequence when we find a number that has NO predecessor (num-1 not in set)
    # This ensures we count each consecutive sequence exactly once, starting from its smallest value
    # For each valid starting number we count how many consecutive numbers exist by checking +1, +2, ...
    # Track the maximum length found across all starting points

    # Time: O(n) - scales linearly with the size of nums arr, Space: O(n) - also scales linearly with size of nums arr

        # if nums is empty, just return 0
        maxConsecLen = 0
        if not nums:
            return maxConsecLen
        # create set from nums arr - this op is O(n)
        numSet = set(nums)
        # iterate over set to avoid duplicates
        for num in numSet:
            currConsecLen = 1
            # if num - 1 not in set, this is potential start of seq
            # else not a potential start of seq, return to for loop and iter to next val in set
            if (num - 1) not in numSet:
                startOfSeq = num
                # start counting from this val while startOfSeq + 1 exists in set
                while (startOfSeq + 1) in numSet:
                    currConsecLen += 1
                    startOfSeq += 1
                # update max counter
                maxConsecLen = max(currConsecLen, maxConsecLen)
        return maxConsecLen

