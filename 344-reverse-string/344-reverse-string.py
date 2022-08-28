class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        stop_point = len(s) // 2
        p1 = 0
        p2 = -1
        while p1 < stop_point: 
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp 
            p1 += 1
            p2 -= 1
        return s