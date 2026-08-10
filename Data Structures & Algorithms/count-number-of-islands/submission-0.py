class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def recurse(x, y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == "0":
                return

            grid[x][y] = "0"

            recurse(x + 1, y)
            recurse(x - 1, y)
            recurse(x, y + 1)
            recurse(x, y - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    recurse(i, j)
                    islands += 1
        
        return islands

        