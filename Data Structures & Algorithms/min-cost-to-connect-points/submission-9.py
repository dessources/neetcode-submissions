class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        res = 0
        visit = set()
        heap = [(0, 0)]
        while heap and len(visit) < N:
            cost, v = heapq.heappop(heap)
            if v in visit:
                continue
            res += cost
            visit.add(v)

            x1, y1 = points[v]
            for i in range(N):
                if i == v or i in visit:
                    continue
                x2, y2 = points[i]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(heap, (dist, i))

        return res

        