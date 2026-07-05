class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0

        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break

        c = 0
        while True:
            c = nums[c]
            s = nums[s]

            if c == s:
                return c
        