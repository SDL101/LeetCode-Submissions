class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        indexCount = []
        
        for char in s:
            if char == "(":
                indexCount.append(len(res))
            elif char == ")":
                start = indexCount.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(char)
            
        return ''.join(res)