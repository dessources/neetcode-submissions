class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q= deque()

        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j]:
                    q.append((i,j))
        
        dist=1
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for di,dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                    x,y = i+di, j+dj
                    if x<0 or x==ROWS or y<0 or y==COLS or grid[x][y] != INF:
                        continue
                    grid[x][y] = dist
                    q.append((x,y))
            dist+=1
        
            
        
        

        