class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        half = -1* (len(arr)//2)
        freq = {}
        
        for each in arr:
            freq[each] = freq.get(each, 0)+ 1
        
        freqArr = []
        for vals in freq.values():
            freqArr.append(vals *-1)
        heapq.heapify(freqArr)
        
        check = 0
        count = 0
        while check > half:
            count += 1
            check += heapq.heappop(freqArr)
        return count 
        
        
        
        
        