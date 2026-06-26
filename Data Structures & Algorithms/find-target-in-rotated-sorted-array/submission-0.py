class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l=mid+1

        offset = l
        l=0
        r = n-1

        while l<=r:
            mid = (l+r)//2
            index = (mid+offset)%n
            if nums[index]==target:
                return index
            elif nums[index]<target:
                l = mid+1
            else:
                r = mid-1
        
        return -1




        