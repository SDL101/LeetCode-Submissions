class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = 0
        maxAlt = 0
        
        for netgain in gain:
            count += netgain 
            if count > maxAlt:
                maxAlt = count
            
        return maxAlt
            
            