class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        stack = []

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    if i == 0 or i == ROWS-1 or j == 0 or j == COLS-1:
                        board[i][j] = 'T'
                        stack.append((i, j))

        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while stack:
            i, j = stack.pop()

            for di, dj in delta:
                x, y = i+di, j + dj
                if x < 0 or x == ROWS or y < 0 or y == COLS or board[x][y] in 'XT':
                    continue
                board[x][y] = 'T'
                stack.append((x, y))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'T':
                    board[i][j] = 'O'
