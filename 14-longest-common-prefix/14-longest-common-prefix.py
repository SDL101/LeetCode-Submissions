class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        
        for string in enumerate(strs):
            if len(string[1]) < min_length:
                min_length = len(string[1])
        
        longest_prefix = ""
        for i in range(min_length):
            char = strs[0][i]
            for string in strs:
                if string[i] != char: 
                    return longest_prefix
            longest_prefix += strs[0][i]
        return longest_prefix
        
        
        
    

        