class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        n,m = len(a), len(b)

        half_len = (n+m+1)//2
        l, r = 0, n

        while l <= r:
            mid1 = (l+r) // 2
            mid2 = half_len - mid1

            a_left = a[mid1 - 1] if mid1 - 1 >= 0 else float("-inf")
            a_right = a[mid1] if mid1 < n else float("inf")

            b_left = b[mid2- 1] if mid2-1 >=0 else float("-inf")
            b_right = b[mid2] if mid2 < m else float("inf")

            if a_right >= b_left and b_right >= a_left:
                if (n+m)%2:
                    return max(a_left, b_left)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            
            elif a_right < b_left:
                l = mid1 + 1

            else:
                r = mid1 -1
        return 0.0

        