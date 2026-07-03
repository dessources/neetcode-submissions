class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = nums[0]
        s = nums[s]
        f = nums[nums[f]]
        
        while s != f:
            s = nums[s]
            f = nums[nums[f]]
            
        c = nums[0]
        while c != s:
            c = nums[c]
            s = nums[s]
        
        return c