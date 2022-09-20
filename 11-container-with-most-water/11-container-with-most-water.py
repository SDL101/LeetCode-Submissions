class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxCalc = 0
        
        l, r = 0, (len(height) - 1)
        
        while l < r:
            length = r - l
            maxCalc = max(maxCalc, (length * (min(height[l], height[r]))))
            if height[l] >= height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
                          
        return maxCalc
            