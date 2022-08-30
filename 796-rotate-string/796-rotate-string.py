class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # s = "bcdea"
        # goal = "cdeab"
        # True
        i = 0
        while i < len(s):
            temp = s[0]
            s = s[1:]
            s = s + temp
            i += 1
            if s == goal:
                return True
        return False
    
                
            