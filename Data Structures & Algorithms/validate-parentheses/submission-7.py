class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = set(["(", "{", "["])
        matches = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif not stack:
                return False
            elif matches[c] != stack.pop():
                return False
            
        return not stack
        