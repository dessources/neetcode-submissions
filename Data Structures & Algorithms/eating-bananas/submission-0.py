class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r = max(piles)
        min_rate = r
        while l <= r:
            rate = (l+r)//2
            print(rate)
            t = sum([math.ceil(p / rate) for p in piles])
            print(t)
            if t <= h:
                r = rate-1
                min_rate = min(min_rate,rate)
            elif t > h:
                l= rate+1
            
        return min_rate


        