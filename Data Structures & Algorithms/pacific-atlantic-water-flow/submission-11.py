class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from_pacific = set()
        from_atlantic = set()
        oceans = {'a': from_atlantic, 'p': from_pacific}

        ROWS, COLS = len(heights), len(heights[0])
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

        def dfs(i, j, ocean):
            if (i, j) in oceans[ocean]:
                return
            oceans[ocean].add((i, j))

            h = heights[i][j]

            for k in range(len(dx)):
                x, y = i + dx[k], j + dy[k]
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or heights[x][y] < h:
                    continue
                dfs(x, y, ocean)

        # get pacific n atlantic cells:
        for col in range(COLS):
            dfs(0, col, "p")
            dfs(ROWS-1, col, "a")

        for row in range(ROWS):
            dfs(row, 0, "p")
            dfs(row, COLS-1, "a")

        result = []

        return [[i, j] for i, j in from_pacific if (i, j) in from_atlantic]