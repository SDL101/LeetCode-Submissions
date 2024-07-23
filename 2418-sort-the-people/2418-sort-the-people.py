class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        #create a heap
        heap = []
        
        #iterate through both names and heights at same time 
        #adding (height, names) to the heap 
        for i in range(len(names)):
            heapq.heappush(heap, (heights[i], names[i]))
        
        #create a deque and 
        #pop of the heap (unpack) one by one and append 
        #just the name to left to the deque
        dq = collections.deque()
        for i in range(len(names)):
            height, name = heapq.heappop(heap)
            dq.appendleft(name)
            
        #return the deque (do I need to convert to list?)
        # return dq
        return(list(dq))