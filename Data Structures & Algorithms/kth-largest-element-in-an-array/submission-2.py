class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n,k = len(nums), len(nums) - k

        def quickSelect(l, r):
            pivot, cur = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[cur] = nums[cur], nums[i]
                    cur += 1
            nums[cur], nums[r] = pivot, nums[cur]

            if cur > k : return quickSelect(l, cur-1)
            if cur < k : return quickSelect(cur+1, r)
            return nums[cur]

        
        return quickSelect(0, n-1)