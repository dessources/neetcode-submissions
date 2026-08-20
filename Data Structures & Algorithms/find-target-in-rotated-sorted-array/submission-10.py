class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            num = nums[mid]

            if num == target:
                return mid
            if num < nums[r]:
                if num < target and target <= nums[r]:
                    l = mid+1
                elif num > target and target < nums[r] or num < target and target > nums[r]:
                    r = mid-1
            else:
                if num < target or target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return -1




        