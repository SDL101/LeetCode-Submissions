class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a new string for the output result
        res = ''
        # loop through each char in the string
        for char in s:
            # if the char is alphanumeric (A-Z, a-z, 0-9)
            if char.isalnum():
                # convert to lowercase and then add to the output
                res += char.lower()
        # return the comparison of the forward and backward result string
        return res == res[::-1]
        