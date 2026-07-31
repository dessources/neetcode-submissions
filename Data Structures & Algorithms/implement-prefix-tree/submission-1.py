class PrefixTree:

    def __init__(self):
        self.arr = [False]*27
    
    def getIdx(self, c: str)->int:
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        cur = self.arr
        for c in word:
            idx = self.getIdx(c)
            if not cur[idx]:
                cur[idx] = [False]*27
            cur = cur[idx]
        cur[26] = True

    def search(self, word: str) -> bool:
        cur = self.arr
        for c in word:
            idx = self.getIdx(c)
            if not cur[idx]:
                return False
            cur = cur[idx]
        return cur[26]
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.arr
        for c in prefix:
            idx = self.getIdx(c)
            if not cur[idx]:
                return False
            cur = cur[idx]
        return True
        