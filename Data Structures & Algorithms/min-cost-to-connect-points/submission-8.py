class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n= len(points)
        seen = set()
        res = 0

        heap = [(0,0)]
        while heap and len(seen)<n:
            # print(heap)
            # print(seen)
            cost, v = heapq.heappop(heap)
            if v in seen:
                continue
            seen.add(v)
            res += cost
            a = points[v]
            ai, aj = a[0], a[1]
          
            for i in range(n):
                if i in seen or i == v:
                    continue
                b = points[i]
                bi, bj = b[0], b[1]
                d = abs(ai-bi) + abs(aj-bj)
                heapq.heappush(heap, (d, i))
            # print("after adding neighbors", seen)
     
        return res

        