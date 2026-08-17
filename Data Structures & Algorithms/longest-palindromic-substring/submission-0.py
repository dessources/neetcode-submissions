class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = (0,1)
        if len(s) == 2 and s[0] == s[-1]:
            return s

        n = len(s)
        def findPalindrome(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -=1
                right += 1
            
            return (left+1, right)

        for i in range(0,len(s)):
            odd = findPalindrome(i,i)
            even = findPalindrome(i,i+1)

            if odd[1]-odd[0] > ans[1]-ans[0]:
                ans = odd
            if even[1] - even[0] > ans[1]-ans[0]:
                ans = even
        
        return s[ans[0]:ans[1]]