class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            leftLowered, rightLowered = s[l].lower(), s[r].lower()
            isLeftAlnum, isRightAlnum = s[l].isalnum(), s[r].isalnum()

            if isLeftAlnum and not isRightAlnum:
                r -= 1
            elif isRightAlnum and not isLeftAlnum:
                l += 1
            elif (isLeftAlnum and isRightAlnum) and (leftLowered != rightLowered):
                return False
            else: 
                l += 1
                r -= 1
        return True
         