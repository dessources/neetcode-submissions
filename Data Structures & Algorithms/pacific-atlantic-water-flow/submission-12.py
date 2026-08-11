class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p, a = set(), set()

        def dfs(i,j, ocean):
            if (i,j) in ocean:
                return
            ocean.add((i,j))
            
            h = heights[i][j]
            for di, dj in [(0,1), (1,0), (0,-1),(-1,0)]:
                x,y=i+di, j+dj
                if x < 0 or x >= ROWS or y <0 or y >= COLS or heights[x][y] < h:
                    continue
                dfs(x,y, ocean)
        
        for r in range(ROWS):
            dfs(r, 0, p)
            dfs(r, COLS-1, a)
        
        for c in range(COLS):
            dfs(0, c, p)
            dfs(ROWS-1, c, a)

        return [[i,j] for i,j in p if (i,j) in a]

        