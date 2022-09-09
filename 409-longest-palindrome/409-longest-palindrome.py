class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        char_freq = {}
        longest_pal = 0
        
        for char in s:
            if char in char_freq:
                char_freq[char] = (char_freq[char] + 1)
            else:
                char_freq[char] = 1
        
        for each in char_freq.keys():
            if char_freq[each] % 2 == 0:
                longest_pal += char_freq[each]
            elif char_freq[each] % 2 == 1:
                if longest_pal % 2 == 0:
                    longest_pal += char_freq[each]
                else:
                    longest_pal += (char_freq[each] - 1)
        
        return longest_pal
    
            