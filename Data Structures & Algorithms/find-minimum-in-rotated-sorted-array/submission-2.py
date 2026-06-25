class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        m = (l+r)//2

        while l<=r:
            num = nums[m]
            if num >= nums[l] and num > nums[r]:
                l = m+1
            elif l==r or num < nums[m-1] and num < nums[m+1]:
                return num
            else:
                r = m-1
            m = (l+r)//2
        return nums[m]
            
        