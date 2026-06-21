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
            s_count[s[r]] = s_count.get(s[r], 0)+1
            if s[r]  in t_count and t_count[s[r]] == s_count[s[r]]:
                have+=1
                while have == need:
                    print(s[l:r+1])
                    if result:
                        result= min(result, (l,r),key=lambda t:t[1]-t[0])
                    else:
                        result =(l,r)
                    
                    s_count[s[l]]-=1
                    if s[l] in t_count and t_count[s[l]] > s_count[s[l]]:
                        have-=1
                    result= min(result, (l,r),key=lambda t:t[1]-t[0])
                    l+=1
                        
        if result:
            return s[result[0]: result[1]+1]
        return ""




        