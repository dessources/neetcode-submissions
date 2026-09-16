class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        
        res = []
        stack = ["JFK"]
        while stack:
            node = stack[-1]
            if adj[node]:
                nxt = heapq.heappop(adj[node])
                stack.append(nxt)
            else:
                res.append(stack.pop())
        print(res)
        return res[::-1]
                
        