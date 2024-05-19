class Solution:
    def reverseWords(self, s: str) -> str:
        splitStr = s.split()
        # print(splitStr)
        output = " ".join(splitStr[::-1])
        return output
    
        