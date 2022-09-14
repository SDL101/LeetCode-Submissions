class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(",
                       "}":"{",
                       "]":"["}
        
        brack_stack = []
        
 
        # s = "(]"
        for char in s:
            if char in closeToOpen.keys() and len(brack_stack) == 0:
                return False
            elif char in closeToOpen.keys():
                if brack_stack[-1] == closeToOpen[char]:
                    brack_stack.pop()
                else:
                    return False
                    
            elif char in closeToOpen.values():
                brack_stack.append(char)
            
        if len(brack_stack) > 0:
            return False
        else:
            return True