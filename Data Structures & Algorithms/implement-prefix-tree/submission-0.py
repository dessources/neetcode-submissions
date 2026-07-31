class PrefixTree:

    def __init__(self):
        self.arr = [None]*27

    def insert(self, word: str) -> None:
        orda = ord('a')
        cur = self.arr
        for c in word:
            idx  = ord(c) - orda
            if not cur[idx]:
                cur[idx] = [None]*27
            cur = cur[idx]
        cur[26] = True

    def search(self, word: str) -> bool:
        orda = ord('a')
        cur = self.arr
        for c in word:
            idx = ord(c) - orda
            if not cur[idx]:
                return False
            cur = cur[idx]
        return bool(cur[26])
        

    def startsWith(self, prefix: str) -> bool:
        orda = ord('a')
        cur = self.arr
        for c in prefix:
            idx = ord(c) - orda
            if not cur[idx]:
                return False
            cur = cur[idx]
        return True
        