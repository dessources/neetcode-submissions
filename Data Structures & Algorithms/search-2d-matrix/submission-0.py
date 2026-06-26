class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        r = (r* c)-1

        while l <= r:
            m = (l+r)//2
            num =matrix[m//c][m%c]

            if num > target:
                r = m-1
            elif num < target:
                l = m+1
            else:
                return True
        
        return False
        