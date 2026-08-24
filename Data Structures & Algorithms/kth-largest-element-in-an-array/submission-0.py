class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for i in range(1,k):
            heapq.heappop(heap)
        
        return -heap[0]
        