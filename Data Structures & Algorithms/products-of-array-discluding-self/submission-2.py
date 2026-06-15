class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)
        arr = [1]*n

        for i in range(1, n):
            arr[i] = arr[i-1] * nums[i-1]
        p=1
        for i in range(2, n+1):
            p*=nums[-i+1]
            arr[-i] *= p
    
        return arr
        