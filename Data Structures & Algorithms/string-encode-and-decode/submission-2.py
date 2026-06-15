from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "%" +s
        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []

        n = ""
        token = ""

        count = 0
        find_len = True
        for c in s:
            if find_len:
                if c != "%":
                    n+=c
                else:
                    find_len = False
            elif count < int(n):
                token+=c
                count +=1
            else:
                result.append(token)
                token = ""
                find_len = True
                count = 0
                n = c
        result.append(token)
        return result