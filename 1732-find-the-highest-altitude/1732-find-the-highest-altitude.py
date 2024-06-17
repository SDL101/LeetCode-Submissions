class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altList = [0]
        count = 0
        maxGain = 0
        
        for netgain in gain:
            count += netgain
            maxGain = max(maxGain, count)
            altList.append(count)
            
        return maxGain
            
            