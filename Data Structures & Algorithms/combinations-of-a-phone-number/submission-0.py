class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        path = []
        def backtrack(i):
            if i >= n:
                if path: result.append("".join(path))
                return
            
            for c in keypad[digits[i]]:
                path.append(c)
                backtrack(i+1)
                path.pop()
        
        backtrack(0)
        
        return result

