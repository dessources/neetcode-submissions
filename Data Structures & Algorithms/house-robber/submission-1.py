class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        loot = [0] * n

        if n <=2:
            return max(nums)

        a, b ,c = 0, 0, 0
        for i in range(n-1, -1, -1):
            loot[i] = nums[i] + max(b,c)
            c = b
            b = a
            a = loot[i]
             
        return max(a,b)


        