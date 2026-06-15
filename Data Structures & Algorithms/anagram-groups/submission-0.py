class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = dict()

        for s in strs:
            key = "".join(sorted([c for c in s]))

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())