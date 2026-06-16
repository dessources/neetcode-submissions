class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        NINE = 9
        rows = []
        cols = []
        squares = []

        for i,row in enumerate(board):
            rows.append(set())
                           
            if i//3 >= len(squares):
                squares.append([])

            for j,col in enumerate(row):
                
                if col.isalnum():
                    if col in rows[i]:
                        print(f"row {i} has duplicate numbers")
                        return False
                    else:
                        rows[i].add(col)

                if j < len(cols):
                    if col in cols[j]:
                        print(f"{col} is in the {j} column twice")
                        print(cols)
                        return False
                    else:
                        if col.isalnum():
                            cols[j].add(col)
                else:
                    cols.append(set())
                    if col.isalnum():
                        cols[-1].add(col)
            
                if j//3 >= len(squares[i//3]):
                    squares[i//3].append(set())
                    if col.isalnum():
                        squares[i//3][j//3].add(col)

                elif col in squares[i//3][j//3]:
                    print(f"{col} is in the ({i//3},{j//3}) square twice")
                    return False
                elif col.isalnum():
                    squares[i//3][j//3].add(col)
        
        return True


        