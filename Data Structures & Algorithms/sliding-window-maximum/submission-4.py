class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        result = []
        l = 0

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if r - l + 1 == k:
                result.append(nums[q[0]])
                l+=1
                if l > q[0]:
                    q.popleft()
        return result
