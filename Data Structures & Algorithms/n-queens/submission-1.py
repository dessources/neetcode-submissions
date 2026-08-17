class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols, pos_d, neg_d = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        board = []

        def backtrack(row):
            if row >= n:
                result.append(board.copy())
            
            for j in range(n):
                if cols[j] or pos_d[row-j] or neg_d[row+j]:
                    continue

                board.append((j * ".") + "Q" + (n-j-1) * ".")
                cols[j], pos_d[row-j] , neg_d[row+j] =  True, True, True
                backtrack(row+1)

                board.pop()
                cols[j], pos_d[row-j] , neg_d[row+j] =  False, False, False

        
        backtrack(0)
        return result
        