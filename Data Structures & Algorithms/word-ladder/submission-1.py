
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        k = len(beginWord)
        seen = set()
        words = set(wordList)
        if endWord not in words:
            return 0

        adj = defaultdict(list)

        words.add(beginWord)
        for w in words:
            for i in range(k):
                pattern = w[:i] + '*' + w[i+1:]
                adj[pattern].append(w)

        def getNeighs(cur):
            res = []
            for i in range(k):
                pattern = cur[:i] + '*' + cur[i+1:]
                for nxt in adj[pattern]:
                    if nxt not in seen:
                        res.append(nxt)
            return res

        seen.add(beginWord)
        q = deque([beginWord])
        res = 2  # minimum two words if a solution exists
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                neighs = getNeighs(cur)
                for neigh in neighs:
                    if neigh == endWord:
                        return res
                    q.append(neigh)
                    seen.add(neigh)
            res += 1
        return 0
                



        
        

        