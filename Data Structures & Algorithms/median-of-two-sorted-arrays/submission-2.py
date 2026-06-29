class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_a, len_b = len(nums1), len(nums2)
        a,b, len_a,len_b= (nums1, nums2, len_a, len_b) if len_a < len_b else (nums2, nums1, len_b, len_a)
        half_len = (len_a + len_b+1) //2

        l, r = 0, len_a

        while l<=r:
            mid_1 = (l+r) // 2
            mid_2 = half_len - mid_1
            a_left  = a[mid_1 - 1] if mid_1 -1 >= 0 else float("-infinity")
            b_left  = b[mid_2 - 1] if mid_2 -1 >= 0 else float("-infinity")
            a_right = a[mid_1]     if mid_1 < len_a else float("infinity")
            b_right = b[mid_2]     if mid_2  < len_b  else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if (len_a + len_b) % 2:
                    return max(a_left, b_left)
                return (max(a_left, b_left) + min(b_right, a_right)) / 2

            elif b_left > a_right:
                l =  mid_1 + 1
            else:
                r = mid_1 - 1
        
        return 0.0
        