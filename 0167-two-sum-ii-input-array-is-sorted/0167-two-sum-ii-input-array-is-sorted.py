class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 0. Problem notes - arr sorted in non-dec ord, convert to 1-indexed arr for output, exactly one solution
        #                  - must use const extra space

        # 1. The sorting makes me think we can use 2 pts to find the two indices


        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                l += 1
                r += 1
                indexArr = [l, r]
                return indexArr
            elif currSum > target:
                r -= 1
            elif currSum < target:
                l += 1






# Time Complexity:

# Space Complexity: 