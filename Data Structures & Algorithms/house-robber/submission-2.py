class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=2:
            return max(nums)

        a, b ,c = 0, 0, 0
        for i in range(n-1, -1, -1):
            tmp1, tmp2 = a, b
            a = nums[i] + max(b,c)
            b = tmp1
            c = tmp2

    
             
        return max(a,b)


        