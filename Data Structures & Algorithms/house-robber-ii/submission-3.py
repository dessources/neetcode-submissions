class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def robber(start, end):
            n = end-start
            a = b= c = 0

            if n <=2:
                return max(nums)

            for i in range(end-1, start-1, -1):
                tmp1, tmp2 = a, b
                a = nums[i] + max(b,c)
                b = tmp1
                c = tmp2

            return max(a,b)
        
        return max(robber(0,n-1), robber(1,n))