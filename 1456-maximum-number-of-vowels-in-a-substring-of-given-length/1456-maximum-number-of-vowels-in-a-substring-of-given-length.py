from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowSet = set('aeiou')
        currWindow = deque()
        currVowCount,  maxVowCount  = 0, 0
        
        for i in range(0, k):
            if s[i] in vowSet:
                currVowCount += 1
            currWindow.append(s[i])
        maxVowCount = max(currVowCount, maxVowCount)
        
        for i in range(k, len(s)):
            if s[i] in vowSet:
                currVowCount += 1
            currWindow.append(s[i])
            
            if currWindow[0] in vowSet:
                currVowCount -= 1
            currWindow.popleft()
            maxVowCount = max(currVowCount, maxVowCount)
            
        return maxVowCount
        