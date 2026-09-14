class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v, t))
        
        state = {}
        heap=[(0,k)]
        delay = 0

        while heap and len(state) < n:
            time, node = heapq.heappop(heap)
            if node in state:
                continue
            state[node] = 1
            delay = time
      
            neighbors = adj[node]
            for v, t in neighbors:
                if v not in state:
                    heapq.heappush(heap, (time+t, v))
        
        return delay if len(state) == n else -1