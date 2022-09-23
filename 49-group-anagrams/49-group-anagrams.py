class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        output = []
        
        for s in strs:
            buckets = [0] * 26
            for char in s:
                bi = ord(char) - ord("a")
                buckets[bi] += 1
                
            count[tuple(buckets)].append(s)
                
        for eachlist in count.values():
            output.append(eachlist)
            
        return output 