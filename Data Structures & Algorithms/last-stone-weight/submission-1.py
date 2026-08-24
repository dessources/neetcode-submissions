class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            c = abs(a-b)
            if c: heapq.heappush(heap, -c)
        
        return -heap[0] if heap else 0