# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        cur = n//2
        
        head = 1 
        tail = n
        
        if n == 1:
            return n
        
        while head < tail:
            if isBadVersion(cur) is False:
                if cur < n and isBadVersion(cur + 1) is True:
                    return cur + 1
                head = cur
                cur = ((head + tail) // 2 ) + 1
            elif isBadVersion(cur) is True:
                if cur == 1 or isBadVersion(cur - 1) is False:
                    return cur
                tail = cur
                cur = tail // 2
                
                
            
            
    
    