class Solution:
    def reverseWords(self, s: str) -> str:
        splitStr = s.split()
        output = " ".join(splitStr[::-1])
        return output
    
        