class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len_a, len_b = len(nums1), len(nums2)
        half_len = (len_a + len_b +1)//2
        l, r = 0, len_a

        while l<=r:
            mid_1 = (l+r) // 2
            mid_2 = half_len - mid_1
            a_left  = nums1[mid_1 - 1] if mid_1 -1 >= 0 else float("-inf")
            b_left  = nums2[mid_2 - 1] if mid_2 -1 >= 0 else float("-inf")
            a_right = nums1[mid_1]     if mid_1 < len_a else float("inf")
            b_right = nums2[mid_2]     if mid_2  < len_b  else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (len_a + len_b) % 2:
                    return max(a_left, b_left)
                return (max(a_left, b_left) + min(b_right, a_right)) / 2

            elif b_left > a_right:
                l =  mid_1 + 1
            else:
                r = mid_1 - 1
        
        return 0.0
        