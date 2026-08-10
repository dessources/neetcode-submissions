
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        delta_x, delta_y = [1, 0, -1, 0], [0, 1, 0, -1]
        n, m = len(board), len(board[0])
        seen = set()
        result = set()

        hm = {}

        def insert(word: str) -> None:
            cur = hm
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["."] = True

        for word in words:
            insert(word)

        def recurse(i, j, path, node):
            c = board[i][j]
            if c not in node:
                return

            next_node = node[c]
            path += c

            if "." in next_node:
                result.add(path)

            seen.add((i, j))
            for k in range(len(delta_x)):
                x, y = delta_x[k]+i, delta_y[k]+j
                if x < n and x >= 0 and y < m and y >= 0 and (x, y) not in seen:
                    recurse(x, y, path, next_node)

            seen.remove((i, j))

        for i in range(n):
            for j in range(m):
                recurse(i, j, "", hm)

        return [word for word in result]
