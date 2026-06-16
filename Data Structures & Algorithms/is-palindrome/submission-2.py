
class Solution:

    def isPalindrome(self, s: str) -> bool:
        if(len(s)) == 1:
            return True
        s = s.lower()
        left = 0
        right = len(s) - 1

        def fix_bounds(is_left, b):
            while b in range(len(s)) and (s[b] == " " or not s[b].isalnum()):
                if is_left:
                    b+=1
                else:
                    b-=1
            return b

        left = fix_bounds(True, left)
        right = fix_bounds(False, right)

        while left <= right:
            if s[left] != s[right]:
                return False
            left +=1
            left = fix_bounds(True, left)
            right-=1
            right = fix_bounds(False, right)
        return True
