
class MedianFinder:

    def __init__(self):
        self.a = []
        self.b = []
        self.n = 0


    def addNum(self, num: int) -> None:
        left = self.a[0] if self.a else float('-inf')
        right = self.b[0] if self.b else float('inf')

        if num <= left or num < right:
            heapq.heappush(self.a, -num)
        else:
            heapq.heappush(self.b, num)

        less, more = (self.a, self.b) if len(self.a) < len(self.b) else (self.b, self.a)
        if abs(len(less) - len(more)) > 1:
            val = heapq.heappop(more)
            heapq.heappush(less, -val)
        
        self.n +=1


    def findMedian(self) -> float:
        if self.a and self.b:
            if self.n%2:
                return -self.a[0] if len(self.a) > len(self.b) else self.b[0]
            return (-self.a[0] + self.b[0]) / 2
        
        return -self.a[0] if self.a else self.b[0]
        
        