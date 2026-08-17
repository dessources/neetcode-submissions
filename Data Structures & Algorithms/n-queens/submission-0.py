class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols, pos_d, neg_d = set(), set(), set()
        board = []

        def backtrack(row):
            if row >= n:
                result.append(board.copy())
            
            for j in range(n):
                cur_col, cur_posd, cur_negd = j, row-j, row+j
                if cur_col in cols or cur_posd in pos_d or cur_negd in neg_d:
                    continue

                board.append((j * ".") + "Q" + (n-j-1) * ".")
                cols.add(cur_col)
                pos_d.add(cur_posd)
                neg_d.add(cur_negd)
                backtrack(row+1)

                board.pop()
                cols.remove(cur_col)
                pos_d.remove(cur_posd)
                neg_d.remove(cur_negd)
        
        backtrack(0)
        return result
        