class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFreq = {}
        tFreq = {}
        for char in s:
            if char in sFreq.keys():
                sFreq[char] += 1
            else:
                sFreq[char] = 1
        for char in t:
            if char in tFreq.keys():
                tFreq[char] += 1
            else:
                tFreq[char] = 1
                
        if sFreq == tFreq:
            return True
        else:
            return False
                
            