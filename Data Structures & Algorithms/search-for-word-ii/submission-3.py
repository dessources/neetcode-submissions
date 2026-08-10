

class PrefixTree:
    def __init__(self):
        self.hm = {}

    def insert(self, word: str) -> None:
        cur = self.hm
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["."] = True

    def search(self, word: str) -> bool:
        cur = self.hm
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "." in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.hm
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        delta_x, delta_y = [1, 0, -1, 0], [0, 1, 0, -1]
        n, m = len(board), len(board[0])
        seen = set()
        result = set()

        trie = PrefixTree()
        for word in words:
            trie.insert(word)

        def recurse(i, j, path):
            if trie.search(path):
                result.add(path)

            if not trie.startsWith(path):
                return

            seen.add((i, j))
            for k in range(len(delta_x)):
                x, y = delta_x[k]+i, delta_y[k]+j
                if x < n and x >= 0 and y < m and y >= 0 and (x, y) not in seen:
                    recurse(x, y, path + board[x][y])

            seen.remove((i, j))

        for i in range(n):
            for j in range(m):
                recurse(i, j, board[i][j])

        return [word for word in result]