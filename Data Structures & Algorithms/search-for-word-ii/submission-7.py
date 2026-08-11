class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = {}
        seen = set()
        result = set()

        for word in words:
            cur  = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["."] = True
        
        def dfs(i, j, path, node):
            if "." in node:
                result.add(path)
                
            if i < 0 or i >= ROWS or j < 0 or j>= COLS or (i,j) in seen:
                return


            c = board[i][j]
            if c not in node:
                return
            
            next_node = node[c]
            path +=c
            seen.add((i,j))
            dfs(i+1,j, path, next_node)
            dfs(i-1,j, path, next_node)
            dfs(i, j+1, path, next_node)
            dfs(i, j-1, path, next_node)
            seen.remove((i,j))
            

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j, '', trie)
                if len(result) == len(words): break
        return list(result)
