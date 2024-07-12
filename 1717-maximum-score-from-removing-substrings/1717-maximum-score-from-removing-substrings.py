class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        points = 0
        
        if x >= y:
            top = 'a'
            comp = 'b'
            firstPass = x
            secondPass = y
        else:
            top = 'b'
            comp = 'a'
            firstPass = y
            secondPass = x
        
        stack = []
        for char in s:
            if stack and char == comp and stack[-1] == top:
                stack.pop()
                points += firstPass
            else:
                stack.append(char)
                
        remStack = []                     
        for char in reversed(stack):
            if remStack and char == comp and remStack[-1] == top:
                remStack.pop()
                points += secondPass 
            else:
                remStack.append(char)
          
        return points