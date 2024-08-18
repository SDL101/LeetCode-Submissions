class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = Counter(s), Counter(t)
        return sMap == tMap