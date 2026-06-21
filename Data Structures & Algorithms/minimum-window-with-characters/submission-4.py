class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        t_count = dict(Counter(t))
        s_count = {}
        result = None
        need = len(t_count)
        have = 0

        l=0
        for r in range(len(s)):
            c=s[r]
            s_count[c] = s_count.get(c, 0)+1
            if c  in t_count and t_count[c] == s_count[c]:
                have+=1
                while have == need:
                    if result:
                        result= min(result, (l,r),key=lambda t:t[1]-t[0])
                    else:
                        result =(l,r)
                    c=s[l]
                    s_count[c]-=1
                    if c in t_count and t_count[c] > s_count[c]:
                        have-=1
                    result= min(result, (l,r),key=lambda t:t[1]-t[0])
                    l+=1
                        
        if result:
            return s[result[0]: result[1]+1]
        return ""




        