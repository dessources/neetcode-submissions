class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        have = {}
        dup_count = 0
        max_sub = 0
        l =0
        for r in range(len(s)):
            have[s[r]] = have.get(s[r],0)+1
            if have[s[r]] > 1:
                dup_count +=1
                
            if dup_count !=0:
                have[s[l]] -=1
                if have[s[l]] != 0:
                    dup_count-=1
                l+=1
            else:
                max_sub = max(max_sub, r-l+1)
            
        return max_sub  