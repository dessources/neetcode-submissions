class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]*len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]

        suf = [1]*len(nums)
        suf[-1] =1

        for i in range(2, len(nums)+1):
            suf[-i] *= suf[-i+1] * nums[-i+1]

        return [pre[i]*suf[i] for i in range(len(nums))]
        