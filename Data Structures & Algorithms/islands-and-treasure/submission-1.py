class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))

        dist = 1
        while q:
            qLen = len(q)
            for _ in range(qLen):
                i,j = q.popleft()
                for di,dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                    x,y = i+di, j+dj
                    if x < 0 or x == ROWS or y < 0 or y == COLS or grid[x][y] in [0,-1] or grid[x][y] != INF:
                        continue
                    grid[x][y] = dist
                    q.append((x,y))
            dist+=1

        
                    
        