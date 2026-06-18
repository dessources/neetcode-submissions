class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hm = {}
        max_count=0
        max_len=0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0)+1
            max_count = max(max_count, hm[s[r]])
            if (r-l+1) - max_count > k:
                hm[s[l]] -=1
                l+=1
            
            max_len = max(max_len, r-l+1)
            
            
        return max_len


        