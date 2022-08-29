class Solution:
    def isPalindrome(self, x: int) -> bool:
        #compare 1st and last indecy values
        #move left pointer up 1 and right pointer down one
        #continue this while left pointer is < len(x) // 2
        #return false if any comparisons don't match
        #return true if loop completes and all comparisons are same
        
        lp = 0 
        rp = -1
        str_x = str(x)
        stop_point = len(str_x) // 2
        while lp < stop_point:
            if str_x[lp] != str_x[rp]:
                return False
            else:
                lp += 1
                rp -=1
        return True