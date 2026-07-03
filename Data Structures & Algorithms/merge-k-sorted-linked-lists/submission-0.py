# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def to_ll(self, nums: List[int])  -> Optional[ListNode]:
        head = ListNode()
        cur = head
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
        
        return self.to_ll(sorted(nums))
        