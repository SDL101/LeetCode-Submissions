class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        chars = []
        
        for char in s:
            if char == "(":
                stack.append(len(chars))
            elif char == ")":
                start = stack.pop()
                chars[start:] = chars[start:][::-1]
            else:
                chars.append(char)
                
        return ''.join(chars)
    
            