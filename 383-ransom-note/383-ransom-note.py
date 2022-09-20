class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magMap = {}
        for char in magazine:
            if char in magMap:
                magMap[char] += 1
            else:
                magMap[char] = 1
            
        
        for c in ransomNote:
            if c not in magMap.keys() or magMap[c] == 0:
                return False
            magMap[c] -= 1
        return True
            