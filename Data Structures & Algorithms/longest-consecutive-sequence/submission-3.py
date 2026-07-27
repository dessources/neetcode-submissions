class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        max_count = 0
        for num in uniq:
            if num -1 not in uniq:
                count = 1
                while num+1 in uniq:
                    count+=1
                    num += 1
                max_count = max(count, max_count)
        return max_count