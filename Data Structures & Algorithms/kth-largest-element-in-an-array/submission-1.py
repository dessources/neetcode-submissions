class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def quickSelect(l, r):
            pivot = nums[r]
            cur = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[cur] = nums[cur], nums[i]
                    cur += 1
            nums[cur], nums[r] = pivot, nums[cur]

            if cur > n-k: return quickSelect(l, cur-1)
            if cur < n-k: return quickSelect(cur+1, r)
            return nums[cur]


        return quickSelect(0, n-1)