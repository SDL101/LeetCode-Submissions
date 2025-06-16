class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            currArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, currArea)
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1
        
        return maxArea