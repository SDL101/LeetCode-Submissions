import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         output = []
#         pointHeap = []
#         for index, point in enumerate(points):
#             x, y = point[0], point[1]
#             dist = math.sqrt((0-x)**2 + (0-y)**2)
#             pointHeap.append([dist,index])
#         heapq.heapify(pointHeap)
        
#         for i in range(k):
#             output.append(points[(heapq.heappop(pointHeap)[1])])
#         return (output)
           points.sort(key = lambda P: P[0]**2 + P[1]**2)
           print(points)
           return points[:k]
            
            