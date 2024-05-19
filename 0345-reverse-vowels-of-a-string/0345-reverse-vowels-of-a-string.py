class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelStr = ""
        outStr = ""
        vowels = set("aeiouAEIOU")
        for char in s:
            if char in vowels:
                vowelStr += char
        i = len(vowelStr) - 1
        for char in s:
            if char not in vowels:
                outStr += char
            else:
                outStr += vowelStr[i]
                i -= 1
        return outStr