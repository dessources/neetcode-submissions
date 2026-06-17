class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif not stack:
                return False
            elif matches[c] != stack.pop():
                return False
            
        return not stack
        