class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = deque([])
        result = []
        l = 0

        for r in range(len(nums)):
            while max_nums and nums[r] > nums[max_nums[-1]]:
                max_nums.pop()
            max_nums.append(r)
            
            if r - l + 1 == k:
                result.append(nums[max_nums[0]])
                l+=1
                if l > max_nums[0]:
                    max_nums.popleft()
        return result
