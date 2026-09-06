class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        delta = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(i,j) -> int:
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
                return 0

            cur_area = 1
            grid[i][j] = 0
            for dx, dy in delta:
                cur_area += dfs(i+dx, j+dy)
            
            return cur_area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    area = max(area, dfs(i,j))
        return area

            
            

        