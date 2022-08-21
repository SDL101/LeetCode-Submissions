class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #input two strings s and t
        #if t is an anagram of s
        #return true
        #else, return false    

        if sorted(s) == sorted(t):
            return True
        return False
        