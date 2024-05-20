from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        charSet = set(word2)
        charMap1 = Counter(word1)
        charMap2 = Counter(word2)
        for keyChar in charMap1.keys():
            if keyChar not in charSet:
                return False
        count1 = Counter(charMap1.values())
        count2 = Counter(charMap2.values())

        # Compare counts of values
        return count1 == count2    