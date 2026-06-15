class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        chars = [0] * 26
        orda = ord('a')
        for c in s:
            chars[ord(c) - orda] +=1

        for c in t:
            chars[ord(c) - orda] -=1
            if chars[ord(c) - orda] < 0:
                return False
        
        return True

        