class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s can be empty 
        #s contains only english letters, digits, symbols and spaces
        #can have upper and lower mixed 
        charSet = set()
        l = 0
        count = 0
        
        # s = "abcabcbb"
        
        for index in range(len(s)):
            while s[index] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[index])
            count = max(count, index - l + 1)
        return count
                
                
                