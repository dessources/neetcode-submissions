class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack  = []
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                prev_h, start = stack.pop()
                max_area = max(max_area, prev_h * (i-start))

            stack.append((h, start))
        
        while stack:
            h, start = stack.pop()
            max_area = max(max_area, h * (n-start))

        return max_area
        