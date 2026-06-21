class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        t_count = dict(Counter(t))
        s_count = {}
        start = end = None
        need = len(t_count)
        have = 0

        l=0
        for r in range(len(s)):
            c=s[r]
            s_count[c] = s_count.get(c, 0)+1
            if c  in t_count and t_count[c] == s_count[c]:
                have+=1
                while have == need:
                    if not start or (start and end-start > r-l+1):
                        start,end = l, r+1
            
                    c=s[l]
                    s_count[c]-=1
                    if c in t_count and t_count[c] > s_count[c]:
                        have-=1
                    l+=1
                    
        return "" if start is None else s[start: end]
        




        