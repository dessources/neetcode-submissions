class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0 
        l = 0
        r = len(height)-1

        max_left = 0
        max_right = 0

        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                water += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                water += max_right - height[r]
                r-=1

        return water
        