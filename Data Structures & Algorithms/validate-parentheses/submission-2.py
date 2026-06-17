class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = set(["(", "{", "["])

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif not stack:
                return False
            elif ord(c) != ord(stack[-1])+1 and ord(c) != ord(stack[-1])+2:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        return False
        