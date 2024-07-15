class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = customers[0][0]
        ave = 0
        
        for c in customers:
            if c[0] > start:
                start = c[0]
            finish = (start + c[1])
            wait = finish - c[0]
            ave += wait
            start = finish
            
        return( ave / len(customers) )