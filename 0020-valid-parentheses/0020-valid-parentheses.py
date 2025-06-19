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
        #    else pop from stack top if closing bracket (or ret false if stack empty) and verify using hashmap
        for bracket in s:
            if bracket in brackMap:
                brackStack.append(bracket)
            elif len(brackStack) == 0:
                return False
            else:
                leftBrack = brackStack.pop()
                if brackMap[leftBrack] != bracket:
                    return False

        # 3. ret False if we still have unclosed brackets, True if stack is empty at the end
        return False if len(brackStack) != 0 else True

    # Time Complexity:  O(n) - we loop through every char in input string, except if we return early. Scales linearly with len of input str
    # Space Complexity: O(n) - our stack scales linearly with the size of the input str, hashmap is constant space