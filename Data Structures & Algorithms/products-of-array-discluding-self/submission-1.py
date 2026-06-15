class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = [1]*len(nums)

        for i in range(1, len(nums)):
            arr[i] = arr[i-1] * nums[i-1]
        p=1
        for i in range(2, len(nums)+1):
            p*=nums[-i+1]
            arr[-i] *= p
    
        return arr
        