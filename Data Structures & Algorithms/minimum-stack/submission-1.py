class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []
        # self.count = 0
        

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
                self.min.append(val)   
        self.arr.append(val)
       

    def pop(self) -> None:
        if self.arr.pop() == self.min[-1]:
            self.min.pop()

        
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]
