class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        getDistance = lambda p: (p[0]**2 + p[1]**2)**.5
        heap =  []

        for p in points:
            d = getDistance(p)
            heapq.heappush(heap, [-d]+p)

            if len(heap)>k:
                heapq.heappop(heap)
        return [[x,y] for d,x,y in heap]
        