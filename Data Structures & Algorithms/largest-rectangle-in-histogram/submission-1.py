class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_rec = 0
        n = len(heights)

        for i,bar in enumerate(heights):
            start = i
            while stack and stack[-1][1] > bar:
                max_rec = max(max_rec, (i - stack[-1][0]) * stack[-1][1])
                start = stack.pop()[0]
            stack.append((start, bar))
        
        while stack:
            max_rec = max(max_rec, (n-stack[-1][0]) * stack.pop()[1])
        
        return max_rec

        