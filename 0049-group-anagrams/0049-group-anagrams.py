class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucketMap = {}

        for word in strs:
            currBucket = [0] * 26
            for char in word:
                mappedIndex = (ord(char) - 97)
                currBucket[mappedIndex] = currBucket[mappedIndex] + 1
            bucketStr = str(currBucket)
            if bucketStr in bucketMap:
                bucketMap[bucketStr].append(word)
            else:
                bucketMap[bucketStr] = [word]
        res = []
        for wordList in bucketMap.values():
            res.append(wordList)
        return res
