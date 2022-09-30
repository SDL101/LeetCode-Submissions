class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        arr = [intervals[0]]
        
        for start, end in intervals[1:]:
            print(start, end)
            if arr[-1][1] >= start:
                arr[-1] = [arr[-1][0], max(arr[-1][1], end)]
            else:
                arr.append([start,end])
        return arr 