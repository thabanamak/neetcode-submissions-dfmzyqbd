import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        org1, org2 = 0, 0
        closest = (0,(0,0))
        distancearray = []
        heapq.heapify(distancearray)
        for point in points:
            x = point[0]
            y = point[1]
            distance = sqrt((x-org1)**2 + (y-org2)**2)
            heapq.heappush(distancearray, (distance, [x,y]))
        answer = []
        while k>0:
            dist, ans = heapq.heappop(distancearray)
            answer.append(ans)
            k-=1
        return answer

            


        