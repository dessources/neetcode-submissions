class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        max_seq = 0

        for num in nums:
            if num-1 not in uniq:
                curr_max = 1
                curr = num+1
                while curr in uniq:
                    curr_max+=1
                    curr+=1
                max_seq=max(curr_max, max_seq)


        return max_seq
            
       

        