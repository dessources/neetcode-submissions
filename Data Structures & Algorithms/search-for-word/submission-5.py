class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        seen = set()

        def backtrack(idx, i,j, count):
            if count == 0:
                return True
            
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i,j) in seen or board[i][j] != word[idx]:
                return False

            seen.add((i,j))
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = i+di, j+dj
                if backtrack(idx+1, x,y, count-1):
                    return True
            seen.remove((i,j))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0,r,c,len(word)):
                    return True
        return False

