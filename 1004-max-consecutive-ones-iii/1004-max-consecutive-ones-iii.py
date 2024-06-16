class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = k
        l, r = 0, 0
        maxLen, currLen = 0, 0
    
        while r < len(nums):
            if nums[r] == 0:
                if flipped > 0:
                    flipped -= 1
                    currLen = r - l + 1
                    r += 1
                else:
                    if nums[l] == 0:
                        flipped += 1
                    l += 1
            else:
                currLen = r - l + 1
                r += 1
            
            maxLen = max(currLen, maxLen)
        
        return maxLen