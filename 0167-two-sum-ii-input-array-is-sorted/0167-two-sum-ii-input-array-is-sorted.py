class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 0. Problem notes - arr sorted in non-dec ord, convert to 1-indexed arr for output, exactly one solution
        #                  - must use const extra space

        # 1. Use 2 ptrs(start and end of arr)
        l, r = 0, len(numbers) - 1
        # 2. While we still have unchecked unique idx pairs and no solutions
        while l < r:
            currSum = numbers[l] + numbers[r]
            # 3. Success case - found two idx's that add to target, inc both for 1-idx output and return
            if currSum == target:
                l += 1
                r += 1
                indexArr = [l, r]
                return indexArr
            # 4. Sum too large case - need to move right ptr down toward smaller numbers (since arr sorted non dec ord)
            elif currSum > target:
                r -= 1
            # 5. Sum too small case - need to move left ptr up toward larger numbers (since arr sorted non dec ord)
            elif currSum < target:
                l += 1

# Time Complexity: O(n) aka Linear - since in the worst case, our iteration of ptrs scales roughly linearly w/ input arr len

# Space Complexity: O(1) aka Constant - since we are only storing the indexArr of len = 2 and the currSum 