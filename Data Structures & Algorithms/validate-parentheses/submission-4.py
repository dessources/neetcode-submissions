class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ["(", "{", "["]
        

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif not stack:
                return False
            elif c==")" and stack[-1] != "(" or c == "]" and stack[-1] != "[" or c == "}" and stack[-1]!="{":
                return False
            else:
                stack.pop()
        if not stack:
            return True
        return False
        