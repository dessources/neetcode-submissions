class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(string, n, open_count, close_count):
            if n == 0:
                if open_count == close_count:
                    result.append(string)
                return
            
            if n > 1:
                backtrack(string + "(", n-1,open_count+1, close_count)
            if open_count > close_count:
                backtrack(string + ")", n -1, open_count, close_count+1)

        backtrack("", n*2, 0, 0)
        return result
        