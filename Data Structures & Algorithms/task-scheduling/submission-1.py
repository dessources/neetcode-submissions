class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        q = deque()
        cycle = 0

        while q or heap:
            cycle+=1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, cycle + n))
            
            if q and q[0][1] == cycle:
                heapq.heappush(heap, q.popleft()[0])
         
        return cycle
                





        