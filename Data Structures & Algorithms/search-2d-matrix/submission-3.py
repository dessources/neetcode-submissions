class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        r = (r* c)-1

        while l <= r:
            m = (l+r)//2
            num =matrix[m//c][m%c]

            if num == target:
                return True
            elif num > target:
                r = m-1
            else:
                l = m+1
                
        
        return False
        