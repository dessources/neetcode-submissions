class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_rec = 0
        n = len(heights)

        for i,bar in enumerate(heights):
            start = i
            while stack and stack[-1][1] > bar:
                area = (i - stack[-1][0]) * stack[-1][1]
                max_rec = max(max_rec, area)
                start = stack[-1][0]
                stack.pop()
            stack.append((start, bar))
        
        while stack:
            max_rec = max(max_rec, (n-stack[-1][0]) * stack[-1][1])
            stack.pop()
        
        return max_rec

        