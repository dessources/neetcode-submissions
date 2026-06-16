
class Solution:

    def isPalindrome(self, s: str) -> bool:
        if(len(s)) == 1:
            return True
        s = "".join([c for c in s.lower() if c.isalnum()])
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
