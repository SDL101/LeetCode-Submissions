class Solution:
    def isValid(self, s: str) -> bool:
        # 0. General Approach - use stack and any time closing bracket encountered, pop from stack
        #                       and check if top of stack is corresponding open bracket or not. return false immediately 
        #                       if there is no match, or if stack is not empty at end of loop, else ret true 

        # 1. create stack for tracking and hashmap for close/open bracket matching
        brackStack = []
        brackMap = {
            '(':')',
            '[':']',
            '{':'}', 
        }

        # 2. loop over the input string and add to stack if open bracket, 
        #    else pop from stack if closing bracket and verify using hashmap
        for bracket in s:
            if bracket in brackMap:
                brackStack.append(bracket)
            elif len(brackStack) == 0:
                return False
            else:
                leftBrack = brackStack.pop()
                if brackMap[leftBrack] != bracket:
                    return False

        return False if len(brackStack) != 0 else True