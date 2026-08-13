class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nodes = {c: [] for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    nodes[w1[j]].append(w2[j])
                    break

        seen, visited = set(), set()
        sorted_order = []

        def dfs(c):
            if c in seen:
                return True
            if c in visited:
                return False

            seen.add(c)
            for neigh in nodes[c]:
                if dfs(neigh):
                    return True

            seen.remove(c)
            visited.add(c)
            sorted_order.append(c)
            return False

        for c in nodes:
            if dfs(c):
                return ""

        sorted_order.reverse()
        return "".join(sorted_order)