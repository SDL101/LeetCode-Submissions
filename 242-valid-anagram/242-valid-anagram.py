class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
       input of two strings s and t 
       if t is an anagram of s (if can rearrange letters to form same word, must use all letters once)
       output true
       if not 
       output false
        
        if s and t aren't same length, automatically return false
        if same length, add chars of each string to an new string after sorting and compare the resulting strings
        if exactly equal, return true
        if not exactly equal, return false
        '''
        
        if len(s) != len(t):
            return False
        
        new_s = ''.join(sorted(s))
        new_t = ''.join(sorted(t))
       
        if new_s == new_t:
            return True
        else:
            return False
            
        
        