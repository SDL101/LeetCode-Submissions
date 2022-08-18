class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPalindrome = False
        str_x = str(x)
        str_x_length = len(str_x)
        if str_x[str_x_length::-1] == str_x:
            isPalindrome = True
        return isPalindrome
     