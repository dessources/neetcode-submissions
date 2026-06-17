class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operate = {
            "+" : lambda a,b: a+b,
            "-" : lambda a,b: a-b,
            "*" : lambda a,b: a*b,
            "/" : lambda a,b: int(a/b)
        }
        operators = ["*", "/", "+", "-"]
        
        stack = []
        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operate[t](a,b))
            else:
                stack.append(int(t))
        
        return stack[-1]