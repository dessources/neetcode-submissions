class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        if endWord not in wordList:
            return 0

        def onlyOne(cur, nxt):
            count=0
            for i in range(len(cur)):
                if cur[i] != nxt[i]:
                    count +=1
                    if count > 1: return False
            return True
         
        q = deque([beginWord])
        res = 2
        while q:
            found=False
            for _ in range(len(q)):
                cur = q.popleft()
                for nxt in wordList:
                    if nxt in seen:
                        continue
                    if onlyOne(cur, nxt):
                        if nxt == endWord:
                            return res
                        q.append(nxt)
                        seen.add(nxt)
                        found=True
            if not found:
                return 0
            res+=1
        return 0
                



        
        

        