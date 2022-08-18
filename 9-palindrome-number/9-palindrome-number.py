class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = False
        str_x = str(x)
        if str_x[::-1] == str_x:
            isPalindrome = True
        return isPalindrome
     