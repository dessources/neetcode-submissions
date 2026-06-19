class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm = {}
        n = len(s1)
        s1_count = dict(Counter(s1))

        l = 0
        for r in range(len(s2)):
            hm[s2[r]] = hm.get(s2[r],0)+1

            if r -l +1 == n:
                if hm == s1_count:
                    return True
            
                hm[s2[l]]-=1
                if hm[s2[l]] == 0:
                    del hm[s2[l]]
                l+=1

        return False


        