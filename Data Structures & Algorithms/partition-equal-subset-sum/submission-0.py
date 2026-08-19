class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total  = sum(nums)
        if total % 2:
            return False
            
        half = total //2
        sums = set()
        sums.add(0)
        n = len(nums)
        for i in range(n-1, -1, -1):
            nextDp = set()
            for t in sums:
                if t+nums[i] == half:
                    return True
                nextDp.add(t)
                nextDp.add(t+nums[i])
            sums = nextDp

        return half in sums
        