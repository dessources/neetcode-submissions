class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        delta_x, delta_y = [1,0,-1,0], [0,1,0,-1]

        def recurse(index, i, j, seen):
            if index == len(word):
                return True
            seen.add((i,j))
            for k in range(len(delta_x)):
                x, y = delta_x[k]+i, delta_y[k]+j
                if x < n and x >= 0 and y < m and y >= 0 and (x,y) not in seen:
                    if board[x][y] == word[index] and recurse(index+1, x, y, set(seen)):
                        return True
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if recurse(1, i, j, set()):
                        return True
        return False
        