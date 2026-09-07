class Solution:
    def solve(self, board: List[List[str]]) -> None:
        Oset = set()
        ROWS, COLS = len(board), len(board[0])
        stack = []

        def dfs(i,j):
            pass
        
        for i in range(ROWS):
            for j in range( COLS):
                if board[i][j] == 'O':
                    if i == 0 or i == ROWS-1 or j == 0 or j == COLS-1:
                        stack.append((i,j))
                    else:
                        Oset.add((i,j))
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        while stack:
            i,j = stack.pop()
       
            for di, dj in delta:
                x, y = i+di, j +dj
                if x < 0 or x == ROWS or y < 0 or y == COLS or board[x][y] == 'X' or (x,y) not in Oset:
                    continue
                Oset.remove((x,y))
                stack.append((x,y))
        
        for i,j in Oset:
            board[i][j] = 'X'
