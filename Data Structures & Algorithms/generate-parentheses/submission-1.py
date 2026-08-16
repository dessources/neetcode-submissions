class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(string, open_count, close_count):
            if len(string) == 2*n:
                result.append(string)
                return
            
            if open_count < n:
                backtrack(string + "(", open_count+1, close_count)
            if open_count > close_count:
                backtrack(string + ")",  open_count, close_count+1)

        backtrack("", 0, 0)
        return result
        