class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str = new_str + char.lower()
        if new_str == new_str[::-1]:
            return True 
        else:
            return False