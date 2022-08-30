class Solution:
    def isValid(self, s: str) -> bool:
        #is input s = "({)}" considered valid?
        
        #create dict with closing bracket as key, and opening bracket as the value
        #create empty stack
        #loop through s
        #if char is an opening bracket, add to stack 
        #if char is a closing bracket, check and see if it's corresponding dict value is on the top of stack
        #if true then pop it off the stack
        #if false, return false
        #once looping is complete, return true if stack is empty
        #return false if stack contains any elements

        brackMap = {")":"(", 
                    "]":"[",
                    "}":"{"}
        
        brackStack = []
        
        # s = "()[]{}"
        #Output: true
        
        # s = "(]"
        #Output: false
        
        for char in s:
            if char not in brackMap.keys():
                brackStack.append(char)
            elif char in brackMap.keys():
                if brackStack and brackStack[-1] == brackMap[char]:
                    brackStack.pop()
                else:
                    return False
            
        if brackStack == []:
            return True
        else:
            return False
        