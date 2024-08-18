class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gramDict = collections.defaultdict(list)
        for string in strs:
            sortString = tuple(sorted(string))
            gramDict[sortString].append(string)
        
        res = []
        for valList in gramDict.values():
            res.append(valList)
        return res