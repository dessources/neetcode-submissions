class Solution:
    def countSubstrings(self, s: str) -> int:
        self.result = n = len(s)

        def findPalindrome(i,j):
            while i >=0 and j < n and s[i] ==s[j]:
                self.result += 1
                i-=1
                j+=1
        
        for i in range(1, n):
            findPalindrome(i-1,i+1)
            findPalindrome(i-1, i)
        
        return self.result
        