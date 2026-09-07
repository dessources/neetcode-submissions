class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0
        FRESH, ROTTEN = 1, 2
       
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                elif grid[i][j] == FRESH:
                    fresh_count +=1

        time = 0
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        while q and fresh_count:
            qLen = len(q)
            for _ in range(qLen):
                i,j = q.popleft()
                for di, dj in delta:
                    x, y = i+di, j+dj
                    if x < 0 or x == ROWS or y < 0 or y==COLS or not grid[x][y] or grid[x][y] == ROTTEN:
                        continue
                    q.append((x,y))
                    grid[x][y] = ROTTEN
                    fresh_count -=1
   
            time +=1
        
        return time if not fresh_count else -1

        