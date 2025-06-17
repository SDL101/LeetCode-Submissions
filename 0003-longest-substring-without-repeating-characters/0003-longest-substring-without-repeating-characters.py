class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubLen = 0
        l, r = 0,  0
        freqSet = set()
        while r < len(s):
            if s[r] not in freqSet:
                freqSet.add(s[r])
                r += 1
            else:
        
                while s[l] != s[r]:
                    freqSet.remove(s[l])
                    l += 1
                if s[l] == s[r]:
                    l += 1
                    r += 1 
            maxSubLen = max(maxSubLen, r - l)
        return maxSubLen