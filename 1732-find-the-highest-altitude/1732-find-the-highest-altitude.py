class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altList = [0]
        count = 0
        
        for netgain in gain:
            count += netgain 
            altList.append(count)
            
        return max(altList)
            
            