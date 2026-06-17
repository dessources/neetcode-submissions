class MinStack:

    def __init__(self):
        self.arr = []
        self.min = None
        

    def push(self, val: int) -> None:
        if self.arr:
            self.arr.append((val,min(val,self.arr[-1][1])))
        else:
            self.arr.append((val,val))
        

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
