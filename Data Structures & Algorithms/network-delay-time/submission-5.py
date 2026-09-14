class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v, t))
        
        state = {}
        heap=[(0,0,0,k)]
        delay = 0

        while heap and len(state) < n:
                prev_time, time, time_added, node = heapq.heappop(heap)
                if node in state:
                    continue
                state[node] = True
                delay += max(0, time-(delay - time_added))
                neighbors = adj[node]
                for v, t in neighbors:
                    if v not in state:
                        heapq.heappush(heap, (prev_time + t, t, delay, v))
                if len(state) == n:
                    break
        
        return delay if len(state) == n else -1